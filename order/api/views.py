from rest_framework import generics
from ..models import TrackOrder, Order
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import ShippingMethod, TrackOrderSerializer, OrderCreateSerializer


class ShippingMethodView(generics.ListAPIView):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethod


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




