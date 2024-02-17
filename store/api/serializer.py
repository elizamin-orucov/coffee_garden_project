from rest_framework import serializers
from ..models import Product, ProductImages


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImages
        fields = (
            "images",
        )


class ProductListSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "name",
            "total_price",
            "price",
            "discount_interest",
            "status",
            "image"
        )

    def get_image(self, obj):
        image = obj.productimages_set.first()
        return ProductImageSerializer(image).data





