from django.urls import path
from . import views

app_name = "accounts_api"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("activation/<uuid>/", views.ActivationView.as_view(), name="activation"),
    path("reset/password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path("change/password/", views.ChangePasswordView.as_view(), name="password_change"),
    path("reset/password/check/<uuid>/", views.ResetPasswordCheckView.as_view(), name="password_reset_check"),
    path("reset/password/complete/<uuid>/", views.ResetPasswordCompleteView.as_view(), name="password_reset_complete"),
]

