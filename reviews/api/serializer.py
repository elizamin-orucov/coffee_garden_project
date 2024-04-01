from ..models import ProductsReview
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsReview
        fields = (
            "id",
            "user",
            "product",
            "parent",
            "message",
            "rating"
        )
        extra_kwargs = {
            "user": {"read_only": True},
            "parent": {"write_only": True}
        }

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        if instance.children.all():
            repr_["replies"] = ReviewSerializer(instance.children.all(), many=True).data
        return repr_

