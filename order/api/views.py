from rest_framework import generics
from rest_framework.response import Response
from services.pagination import CustomPagination
from ..models import TrackOrder, Order, ShippingMethod
from rest_framework.permissions import IsAuthenticated
from .serializer import (
    ShippingMethodSerializer, TrackOrderSerializer, OrderCreateSerializer, OrderListSerializer,
    OrderDetailSerializer
)


class ShippingMethodView(generics.ListAPIView):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer


class TrackOrderView(generics.RetrieveAPIView):
    queryset = TrackOrder.objects.all()
    serializer_class = TrackOrderSerializer
    lookup_field = "order_id"


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "invoice_id"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)






