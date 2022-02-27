from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response

from apps.cores.exceptions import EmailExistException, PasswordCheckException

from .models import User
from .serializers import UserRegisterCheckSerializer, UserRegisterSerializer


class UserRegisterCheckView(generics.CreateAPIView):
    serializer_class = UserRegisterCheckSerializer

    def post(self, request, *args, **kwargs):
        if request.data["password"] != request.data["confirm_password"]:
            raise PasswordCheckException()

        serializer = UserRegisterCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            User.objects.get(email=request.data["email"])
            raise EmailExistException()
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_200_OK)


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.create(**request.data)
        return Response(status=status.HTTP_201_CREATED)
