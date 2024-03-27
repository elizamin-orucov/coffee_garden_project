from ..models import Category
from rest_framework import generics
from .serializer import CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True).order_by("created_at")
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.order_by("created_at")
    serializer_class = CategorySerializer
    lookup_field = "id"




