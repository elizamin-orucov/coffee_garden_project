from . import views
from django.urls import path

app_name = "reviews_api"

urlpatterns = [
    path("create/", views.ReviewView.as_view(), name="review_create"),
    path("edit/<id>/", views.ReviewEditView.as_view(), name="review_edit"),
]
