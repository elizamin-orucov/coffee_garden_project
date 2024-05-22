from . import views
from django.urls import path

app_name = "order_api"

urlpatterns = [
    path("list/", views.OrderListView.as_view(), name="order_list"),
    path("create/", views.OrderCreateView.as_view(), name="order_create"),
    path("track/<order_id>/", views.TrackOrderView.as_view(), name="track_order"),
    path("detail/<invoice_id>/", views.OrderDetailView.as_view(), name="order_detail"),
    path("shipping/methods/", views.ShippingMethodView.as_view(), name="shipping_method"),
]
