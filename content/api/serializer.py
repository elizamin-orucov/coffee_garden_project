from ..models import News, NewsImage
from rest_framework import serializers


class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImage
        fields = (
            "image",
        )


class NewsListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = News
        fields = (
            "slug",
            "image",
            "title",
            "created_at"
        )

    def get_image(self, obj):
        image = obj.newsimage_set.first()
        return NewsImageSerializer(image).data

    def get_created_at(self, obj):
        change_format = obj.created_at.strftime("%d %B %Y")
        return change_format


class NewsDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = News
        fields = (
            "title",
            "images",
            "content",
            "created_at"
        )

    def get_images(self, obj):
        images = obj.newsimage_set.all()
        return NewsImageSerializer(images, many=True).data

    def get_created_at(self, obj):
        change_format = obj.created_at.strftime("%d %B %Y")
        return change_format

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        other_news = News.objects.exclude(id=instance.id)
        repr_["other news"] = NewsListSerializer(other_news, many=True).data
        return repr_


