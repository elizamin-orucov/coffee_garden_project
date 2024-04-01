from . import views
from django.urls import path


app_name = "wishlist"


urlpatterns = [
    path("list/", views.WishListView.as_view(), name="list"),
    path("create/", views.WishListCreateView.as_view(), name="create")
]
