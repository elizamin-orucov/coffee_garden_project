from ..models import WishList
from rest_framework import serializers
from base.api.serializer import CategorySerializer
from store.api.serializer import ProductImageSerializer


class WishListSerializer(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField(read_only=True)
    product_name = serializers.SerializerMethodField(read_only=True)
    product_image = serializers.SerializerMethodField(read_only=True)
    product_price = serializers.SerializerMethodField(read_only=True)
    product_category = serializers.SerializerMethodField(read_only=True)
    product_total_price = serializers.SerializerMethodField(read_only=True)
    product_discount_interest = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = WishList
        fields = (
            "product",
            "product_id",
            "product_name",
            "product_image",
            "product_price",
            "product_total_price",
            "product_discount_interest",
            "product_category",
        )
        extra_kwargs = {
            "product": {"write_only": True}
        }

    def get_product_id(self, obj):
        return obj.product.id

    def get_product_name(self, obj):
        return obj.product.name

    def get_product_image(self, obj):
        image = obj.product.productimages_set.first()
        return ProductImageSerializer(image).data

    def get_product_price(self, obj):
        return obj.product.price

    def get_product_category(self, obj):
        return CategorySerializer(obj.product.category).data

    def get_product_total_price(self, obj):
        discount_price = obj.product.price * (obj.product.discount_interest or 0) / 100
        return obj.product.price - discount_price

    def get_product_discount_interest(self, obj):
        return obj.product.discount_interest



