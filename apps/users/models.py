import random

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import EmailValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from faker import Faker

from apps.cores.models import DeleteModel, TimeStampModel

from .validators import PasswordValidator


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email or not password:
            raise ValueError("The given email or password must be set")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email or not password:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("nickname", "admin")
        superuser = self.model(email=email, **extra_fields)
        superuser.set_password(password)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        superuser.save()
        return superuser


class User(AbstractBaseUser, PermissionsMixin, TimeStampModel, DeleteModel):
    """
    - AbstractBaseUser : password, last_login, is_active
    - PermissionsMixin : is_superuser, groups, user_permissions
    - TimeStampModel : created_at, modified_at
    - DeleteModel : is_deleted, deleted_at
    """

    from .utils import get_nickname

    email = models.EmailField(
        unique=True, validators=[EmailValidator()], verbose_name="이메일"
    )
    password = models.CharField(
        _("password"),
        max_length=128,
        validators=[PasswordValidator()],
    )
    nickname = models.CharField(
        unique=True,
        max_length=64,
        default=get_nickname,
        verbose_name="닉네임",
    )
    is_staff = models.BooleanField(default=False, verbose_name="관리자여부")

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserOption(TimeStampModel, models.Model):
    GENDER_CHOICES = [
        (None, ""),
        ("F", "여"),
        ("M", "남"),
    ]
    user_id = models.OneToOneField(
        User,
        related_name="option",
        on_delete=models.CASCADE,
        db_column="user_id",
    )
    gender = models.CharField(
        blank=True,
        null=True,
        max_length=1,
        choices=GENDER_CHOICES,
        default=None,
        verbose_name="성별",
    )
    height = models.PositiveSmallIntegerField(default=0, verbose_name="키")
    weight = models.PositiveSmallIntegerField(default=0, verbose_name="몸무게")
    is_stand = models.BooleanField(default=False, verbose_name="서서")
    is_sit = models.BooleanField(default=False, verbose_name="앉아서")
    is_balance = models.BooleanField(default=False, verbose_name="밸런스")
    is_core = models.BooleanField(default=False, verbose_name="코어")
    is_arm = models.BooleanField(default=False, verbose_name="팔")
    is_recline = models.BooleanField(default=False, verbose_name="누워서")

    def __str__(self):
        return f"{self.user_id}"


class UserDailyRecord(TimeStampModel, models.Model):
    today = timezone.now()

    user_id = models.ForeignKey(
        User,
        related_name="daily_record",
        on_delete=models.CASCADE,
        db_column="user_id",
    )
    exercise_date = models.DateField(verbose_name="운동 날짜")
    exercise_week = models.PositiveSmallIntegerField(
        default=int(today.isocalendar()[1]), editable=False, verbose_name="주차"
    )
    exercise_duration = models.PositiveSmallIntegerField(
        default=0, verbose_name="일별 총 운동시간"
    )
    calories_total = models.PositiveSmallIntegerField(
        default=0, verbose_name="일별 총 소모칼로리"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "exercise_date"], name="users_userdaily_history"
            )
        ]

    def __str__(self):
        return f"{self.user_id} - {self.exercise_date}"


@receiver(pre_save, sender=UserDailyRecord)
def user_record_pre_save_receiver(sender, instance, *args, **kwargs):
    exercise_date = instance.exercise_date
    instance.exercise_week = exercise_date.isocalendar()[1]
