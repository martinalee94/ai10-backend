from django.utils.translation import gettext_lazy as _
from rest_framework import filters, generics, permissions
from rest_framework.exceptions import ValidationError

from apps.cores.paginations import StandardPageNumberPagination
from apps.cores.permissions import IsOwner
from apps.users.models import UserOption

from .models import BookMark, Course, CourseReview, Exercise
from .serializers import (
    BookMarkSerializer,
    CourseReviewSerializer,
    CourseSerializer,
    ExerciseSerializer,
)

# Create your views here.


class ExerciseDetailView(generics.RetrieveAPIView):
    """
    운동 상세
    """

    name = "Exercise Detail"
    serializer_class = ExerciseSerializer
    pagination_class = StandardPageNumberPagination
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = "standard"
    queryset = Exercise.objects.all()


class CourseListView(generics.ListAPIView):
    """
    코스 리스트(검색 기능 포함)
    """

    name = "Course List"
    serializer_class = CourseSerializer
    pagination_class = StandardPageNumberPagination
    permission_classes = [permissions.AllowAny]
    throttle_scope = "standard"
    queryset = Course.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["course_name", "hash_tag__tag"]


class CourseDetailView(generics.RetrieveAPIView):
    """
    코스의 상세정보(리뷰 미포함)
    """

    name = "Course Detail"
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = "standard"
    queryset = Course.objects.all()


class ReviewListCreateView(generics.ListCreateAPIView):
    """
    코스 리뷰 리스트 및 생성(정렬 기능 포함)
    """

    name = "Course Review List & Create"
    serializer_class = CourseReviewSerializer
    pagination_class = StandardPageNumberPagination
    throttle_scope = "standard"
    permission_classes = [permissions.IsAuthenticated]
    queryset = CourseReview.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["rating", "created_at"]
    ordering = ["-rating"]

    def perform_create(self, serializer):
        """
        코스 평균 평점에 리뷰 평점을 반영
        """
        course_id = self.kwargs.get("pk")
        course = Course.objects.get(pk=course_id)

        user = self.request.user
        review_queryset = CourseReview.objects.filter(course_id=course, user_id=user)

        if review_queryset.exists():
            raise ValidationError("이미 이 코스에 대한 리뷰가 있습니다!")

        if course.count_review == 0:
            course.avg_rating = serializer.validated_data["rating"]

        else:
            course.avg_rating = round(
                (course.avg_rating + serializer.validated_data["rating"]) / 2, 1
            )

        course.count_review += 1
        course.save()

        serializer.save()


class ReviewDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    코스 리뷰 삭제 및 업데이트
    """

    name = "Course Review Read & Update & Delete"
    serializer_class = CourseReviewSerializer
    permission_classes = [IsOwner]
    throttle_scope = "standard"
    queryset = CourseReview.objects.all()


class BookMarkListCreateView(generics.ListCreateAPIView):
    """
    북마크 생성, 조회
    """

    name = "Course BookMark Create"
    serializer_class = BookMarkSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = "standard"

    def get_queryset(self):
        user = self.request.user
        queryset = BookMark.objects.filter(user_id=user)
        return queryset

    def perform_create(self, serializer):
        course_id = serializer.validated_data["course_id"]
        user = self.request.user
        bookmark_queryset = BookMark.objects.filter(user_id=user, course_id=course_id)

        if bookmark_queryset.exists():
            raise ValidationError("이미 이 코스를 북마크 하셨습니다!")

        serializer.save()


class BookMarkDeleteView(generics.DestroyAPIView):
    """
    북마크 삭제
    """

    name = "Course Bookmark Delete"
    serializer = BookMarkSerializer
    permission_classes = [IsOwner]
    throttle_scope = "standard"
    queryset = BookMark.objects.all()


class CourseRecommendView(generics.ListAPIView):
    """
    코스 추천
    """

    name = "Course Recommendation"
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = "standard"

    def get_queryset(self):
        user = self.request.user
        user_option = UserOption.objects.get(user_id=user)
        course = Course.objects.all()
        queryset = None
        if user_option.is_stand:  # must fix: model 변경 후 반드시 수정
            queryset = course.order_by("-stand_count")[:5]
        if user_option.is_sit:
            qs = course.order_by("-sit_count")[:5]
            if queryset is None:
                queryset = qs
            else:
                queryset = queryset | qs
        if user_option.is_balance:
            qs = course.order_by("-balance_count")[:5]
            if queryset is None:
                queryset = qs
            else:
                queryset = queryset | qs
        if user_option.is_core:
            qs = course.order_by("-core_count")[:5]
            if queryset is None:
                queryset = qs
            else:
                queryset = queryset | qs
        if user_option.is_leg:
            qs = course.order_by("-leg_count")[:5]
            if queryset is None:
                queryset = qs
            else:
                queryset = queryset | qs
        if user_option.is_back:
            qs = course.order_by("-back_count")[:5]
            if queryset is None:
                queryset = qs
            else:
                queryset = queryset | qs

        if queryset is None:
            return course.order_by("?")

        return queryset.order_by("?")[0:1]
