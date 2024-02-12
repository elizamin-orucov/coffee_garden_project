from django.contrib.auth.models import BaseUserManager


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

