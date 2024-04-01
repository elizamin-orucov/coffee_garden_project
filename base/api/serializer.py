from ..models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.SerializerMethodField(read_only=True)
    category_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = (
            "category_id",
            "category_name"
        )

    def get_category_id(self, obj):
        return obj.id

    def get_category_name(self, obj):
        return obj.name

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        if instance.children.all():
            repr_["children"] = CategorySerializer(instance.children.all(), many=True).data
        return repr_

