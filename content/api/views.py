from ..models import News
from rest_framework import generics
from services.pagination import CustomPagination
from .serializer import NewsListSerializer, NewsDetailSerializer


class NewsListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = NewsListSerializer
    queryset = News.objects.order_by("-created_at")


class NewsDetailView(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = NewsDetailSerializer
    queryset = News.objects.order_by("-created_at")


