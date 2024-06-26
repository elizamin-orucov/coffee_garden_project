from . import views
from django.urls import path

app_name = "store_api"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product/detail/<slug>/", views.ProductDetailView.as_view(), name="product_detail"),
]
