from . import views
from django.urls import path

app_name = "base_api"

urlpatterns = [
    path("category/list/", views.CategoryListView.as_view(), name="category_list"),
    path("category/detail/<int:id>/", views.CategoryDetailView.as_view(), name="category_detail"),
]
