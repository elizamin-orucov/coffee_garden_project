from rest_framework import generics
from django.utils.encoding import smart_str
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from rest_framework.permissions import IsAuthenticated
from .serializer import (
    LoginSerializer, RegisterSerializer, ActivationSerializer, ResetPasswordSerializer,
    ResetPasswordCheckSerializer, ResetPasswordCompleteSerializer, ChangePasswordSerializer,
    ProfileEditSerializer, ProfileDeleteSerializer, ProfileDeleteCheckSerializer,
)


User = get_user_model()


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ActivationView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ActivationSerializer
    lookup_field = "uuid"

    def get_object(self):
        uuid = self.kwargs.get(self.lookup_field)
        id_ = smart_str(urlsafe_base64_decode(uuid))
        return User.objects.get(id=id_)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ResetPasswordView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer


class ResetPasswordCheckView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordCheckSerializer
    lookup_field = "uuid"

    def get_object(self):
        uuid = self.kwargs.get("uuid")
        id_ = smart_str(urlsafe_base64_decode(uuid))
        return User.objects.get(id=id_)


class ResetPasswordCompleteView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordCompleteSerializer
    lookup_field = "uuid"

    def get_object(self):
        uuid = self.kwargs.get("uuid")
        id_ = smart_str(urlsafe_base64_decode(uuid))
        return User.objects.get(id=id_)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ProfileEditView(generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = ProfileEditSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ProfileDeleteView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = ProfileDeleteSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfileDeleteCheckView(generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = ProfileDeleteCheckSerializer
    lookup_field = "uuid"

    def get_object(self):
        uuid = self.kwargs.get("uuid")
        id_ = smart_str(urlsafe_base64_decode(uuid))
        return User.objects.get(id=int(id_))






