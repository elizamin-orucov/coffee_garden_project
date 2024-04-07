from . import views
from django.urls import path

app_name = "content_api"

urlpatterns = [
    path("news/", views.NewsListView.as_view(), name="news_list"),
    path("news/detail/<slug>/", views.NewsDetailView.as_view(), name="news_detail"),
]
