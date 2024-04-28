from rest_framework import generics
from ..models import TrackOrder, Order
from .serializer import ShippingMethod, TrackOrderSerializer


class ShippingMethodView(generics.ListAPIView):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethod


class TrackOrderView(generics.RetrieveAPIView):
    queryset = TrackOrder.objects.all()
    serializer_class = TrackOrderSerializer




