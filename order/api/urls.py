from . import views
from django.urls import path

app_name = "order_api"

urlpatterns = [
    path("create/", views.OrderCreateView.as_view(), name="order_create"),
    path("track/<order_id>/", views.TrackOrderView.as_view(), name="track_order"),
    path("shipping/methods/", views.ShippingMethodView.as_view(), name="shipping_method"),
]
