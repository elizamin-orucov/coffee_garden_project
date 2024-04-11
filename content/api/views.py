from ..models import News, Event
from rest_framework import generics
from services.pagination import CustomPagination
from .serializer import (NewsListSerializer, NewsDetailSerializer,
                         EventListSerializer, EventDetailSerializer)


class NewsListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = NewsListSerializer
    queryset = News.objects.order_by("-created_at")


class NewsDetailView(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = NewsDetailSerializer
    queryset = News.objects.order_by("-created_at")


class EventListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = EventListSerializer
    queryset = Event.objects.order_by("start_date")


class EventDetailView(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = EventDetailSerializer
    queryset = Event.objects.order_by("start_date")
