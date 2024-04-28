from . import views
from django.urls import path

app_name = "order_api"

urlpatterns = [
    path("shipping/methods/", views.ShippingMethodView.as_view(), name="shipping_method"),

]
