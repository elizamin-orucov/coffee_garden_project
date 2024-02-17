from django.urls import path
from . import views

app_name = "store_api"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list")
]
