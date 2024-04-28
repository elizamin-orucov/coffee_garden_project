from rest_framework import serializers
from services.choices import TRACK_ORDER_STATUS
from ..models import Order, OrderItem, TrackOrder, ShippingMethod


class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = (
            "id",
            "method",
            "duration",
            "price"
        )


class TrackOrderStatusSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = TrackOrder
        fields = (
            "status",
            "date",
        )

    def get_transaction_date(self, obj):
        date_format = obj.order.created_at.strftime("%A, %d %B %Y, %H:%M %p")
        return date_format


class TrackOrderSerializer(serializers.ModelSerializer):
    transaction_date = serializers.SerializerMethodField(read_only=True)
    shipping_method = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = (
            "transaction_date",
            "shipping_method",
            "total_paid",
            "status"
        )

    def get_transaction_date(self, obj):
        return obj.created_at.strftime("%d %B %Y")

    def get_shipping_method(self, obj):
        return ShippingMethodSerializer(obj.shippingmethod_set.first()).data

    def get_status(self, obj):
        status = obj.trackorder_set.order_by("-created_at")
        return TrackOrderStatusSerializer(status, many=True).data



    # class Meta:
    #     model = Order
    #     fields = (
    #         "first_name",
    #         "last_name",
    #         "country",
    #         "city",
    #         "address",
    #         "phone",
    #         "postal_code",
    #         "coupon_discount",
    #         "shipping_method",
    #         "subtotal",
    #         "total_paid"
    #     )
    #     extra_kwargs = {
    #         "coupon_discount": {"write_only": True},
    #     }

