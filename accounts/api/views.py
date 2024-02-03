from rest_framework import generics
from django.utils.encoding import smart_str
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from .serializer import (
    LoginSerializer, RegisterSerializer, ActivationSerializer,
)
from rest_framework.response import Response

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


