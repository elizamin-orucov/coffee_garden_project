from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from services.generator import CodeGenerator


class MyUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        name,
        surname,
        password=None,
        is_active=True,
        is_staff=False,
        is_superuser=False
    ):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.name = name
        user.surname = surname
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name=None, surname=None, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def upload_to(instance, filename):
    return f"users/{instance.email}/{filename}"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=120)
    name = models.CharField(max_length=250, blank=True, null=True)
    surname = models.CharField(max_length=250, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    slug = models.SlugField(unique=True)
    activation_code = models.CharField(max_length=6, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = CodeGenerator.create_slug_shortcode(size=20, model_=self.__class__)
        if not self.logo:
            default_logo_path = "static/user/user.jpg"
            self.logo.save("default_user_logo.jpg", open(default_logo_path, "rb"), save=False)
        return super(User, self).save(*args, **kwargs)


