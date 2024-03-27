from rest_framework import serializers
from ..models import Product, ProductImages
from base.api.serializer import CategorySerializer
from reviews.api.serializer import ReviewSerializer
from django.db.models import IntegerField, F
from django.db.models.functions import Coalesce


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImages
        fields = (
            "images",
        )


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    rating = serializers.FloatField()
    total_price = serializers.FloatField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "rating",
            "slug",
            "category",
            "total_price",
            "price",
            "discount_interest",
            "status",
            "image"
        )

    def get_image(self, obj):
        image = obj.productimages_set.first()
        return ProductImageSerializer(image).data


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    total_price = serializers.FloatField(read_only=True)
    rating = serializers.FloatField(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "rating",
            "category",
            "images",
            "description",
            "status",
            "price",
            "total_price",
            "discount_interest",
        )

    def get_images(self, obj):
        images_list = ProductImageSerializer(obj.productimages_set.all(), many=True).data
        return images_list

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        # obtaining the list of relevant products
        related_list = instance.category.product_set.exclude(id=instance.id).order_by("-created_at")
        repr_["related products"] = ProductListSerializer(related_list, many=True).data
        # list of comments made on the product
        comments_list = instance.productsreview_set.order_by("-created_at")
        repr_["comments"] = ReviewSerializer(comments_list, many=True).data
        return repr_






