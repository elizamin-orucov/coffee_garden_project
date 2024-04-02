from django.db import models
from services.mixin import DateMixin
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class OurLocation(DateMixin):
    location = models.CharField(max_length=300)
    service = PhoneNumberField()
    working_hours = models.CharField(max_length=150)

    def __str__(self):
        return self.location

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.__class__.objects.exclude(id=self.id).delete()

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Our Location"


class AboutUs(DateMixin):
    title = models.CharField(max_length=300)
    about = RichTextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.__class__.objects.exclude(id=self.id).delete()

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Us"


class ContactUs(DateMixin):
    full_name = models.CharField(max_length=30)
    subjects = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=500)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # staff who replied to the message

    def __str__(self):
        return f"Full name: {self.full_name} Subject: {self.subjects}"

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "Contact Us"


class Subscriber(DateMixin):
    email = models.EmailField(unique=True, max_length=150)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "email"
        verbose_name_plural = "Subscribers"



