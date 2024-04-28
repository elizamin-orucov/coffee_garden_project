from ..models import Basket
from rest_framework import generics
from .permission import BasketPermission
from .serializer import BasketSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class BasketListView(generics.ListAPIView):
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # filter to get current user's baskets
        return Basket.objects.filter(user=self.request.user).order_by("created_at")


class BasketCreateView(generics.CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        quantity = self.request.data.get("quantity")
        product_id = self.request.data.get("product")
        # to prevent the same basket from being created again
        basket, created = Basket.objects.get_or_create(
            product_id=int(product_id), user=self.request.user,
            defaults={"quantity": int(quantity)}
        )
        if not created:
            basket.quantity = int(quantity)
            basket.save()
        return Response(self.serializer_class(basket).data)


class BasketEditView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, BasketPermission)
    serializer_class = BasketSerializer
    lookup_field = "id"

    def get_queryset(self):
        # for the current user to update only their own septs
        return Basket.objects.filter(user=self.request.user)

    # since the same serializer will be used in create and upate, the update function has been changed.
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        product_id = obj.product.id
        serializer = self.serializer_class(instance=obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(product_id=product_id)
        return Response(serializer.data)



