from rest_framework import generics, filters
from ..models import Product
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F, IntegerField, Avg, FloatField
from django.db.models.functions import Coalesce
from .serializer import ProductListSerializer, ProductDetailSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.order_by("-created_at")
    serializer_class = ProductListSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
    )
    filterset_class = ProductFilter
    ordering_fields = ("totalprice", "created_at")

    def get_queryset(self):
        qs = self.queryset.annotate(
            dic_interest=Coalesce("discount_interest", 0, output_field=IntegerField()),
            discount_price=F("price") * F("dic_interest") / 100,
            totalprice=F("price") - F("discount_price"),
            rating=Coalesce(Avg("productsreview__rating"), 0, output_field=FloatField())
        ).order_by("-created_at")
        return qs


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.order_by("-created_at")
    serializer_class = ProductDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        qs = self.queryset.annotate(
            rating=Coalesce(Avg("productsreview__rating"), 0, output_field=FloatField())
        ).order_by("-created_at")
        return qs

