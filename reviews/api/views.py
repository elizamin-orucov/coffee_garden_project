from rest_framework import generics
from ..models import ProductsReview
from .serializer import ReviewSerializer
from rest_framework.permissions import IsAuthenticated


class ReviewView(generics.CreateAPIView):
    queryset = ProductsReview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = IsAuthenticated,

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

