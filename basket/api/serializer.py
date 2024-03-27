from store.api.serializer import ProductImageSerializer
from base.api.serializer import CategorySerializer
from rest_framework import serializers
from ..models import Basket


class BasketSerializer(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField(read_only=True)
    product_image = serializers.SerializerMethodField(read_only=True)
    product_name = serializers.SerializerMethodField(read_only=True)
    product_category = serializers.SerializerMethodField(read_only=True)
    product_price = serializers.SerializerMethodField(read_only=True)
    product_subtotal = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Basket
        fields = (
            "id",
            "product",
            "quantity",
            "product_id",
            "product_name",
            "product_image",
            "product_price",
            "product_subtotal",
            "product_category",
        )
        extra_kwargs = {
            "product": {"write_only": True}
        }

    def get_product_id(self, obj):
        return obj.product.id

    def get_product_image(self, obj):
        image = obj.product.productimages_set.first()
        return ProductImageSerializer(image).data

    def get_product_name(self, obj):
        return obj.product.name

    def get_product_category(self, obj):
        category = obj.product.category
        return CategorySerializer(category).data

    def get_product_price(self, obj):
        product_price = obj.product.price
        return product_price

    def get_product_subtotal(self, obj):
        discount_price = obj.product.price * (obj.product.discount_interest or 0) / 100
        return obj.product.price - discount_price


