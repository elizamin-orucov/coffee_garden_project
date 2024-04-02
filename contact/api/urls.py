from . import views
from django.urls import path

app_name = "contact_api"


urlpatterns = [
    path("about-us/", views.AboutUsView.as_view(), name="about_us"),
    path("contact-us/", views.ContactUsView.as_view(), name="contact_us"),
    path("subscriber/", views.SubscriberView.as_view(), name="subscriber"),
    path("our-location/", views.OurLocationView.as_view(), name="our_location")
]

