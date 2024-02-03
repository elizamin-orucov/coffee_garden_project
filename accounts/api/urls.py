from django.urls import path
from . import views

app_name = "accounts_api"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("activation/<uuid>/", views.ActivationView.as_view(), name="activation"),
]

