from ..models import WishList
from rest_framework import generics
from .serializer import WishListSerializer
from rest_framework.response import Response
from services.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated


class WishListView(generics.ListAPIView):
    serializer_class = WishListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)


class WishListCreateView(generics.CreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get("product")
        obj, created = WishList.objects.get_or_create(
            user=request.user, product_id=product_id
        )
        if not created:
            obj.delete()
        serializer = self.serializer_class(obj).data
        return Response(serializer)



