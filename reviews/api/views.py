from rest_framework import generics
from ..models import ProductsReview
from .serializer import ReviewSerializer
from .permission import ReviewPermission
from rest_framework.permissions import IsAuthenticated


class ReviewView(generics.CreateAPIView):
    queryset = ProductsReview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = IsAuthenticated,

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ReviewEditView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = ReviewSerializer
    permission_classes = IsAuthenticated, ReviewPermission

    def get_queryset(self):
        return ProductsReview.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


