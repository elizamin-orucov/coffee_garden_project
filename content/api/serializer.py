from rest_framework import serializers
from ..models import News, NewsImage, Event, EventImages


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


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = (
            "image",
        )


class EventListSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = (
            "slug",
            "title",
            "image",
            "date",
            "status"
        )

    def get_image(self, obj):
        image = obj.eventimages_set.first()
        return EventImageSerializer(image).data

    def get_date(self, obj):
        format = obj.start_date.strftime("%d %h %Y")
        return format


class EventDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    start = serializers.SerializerMethodField(read_only=True)
    end = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = (
            "title",
            "images",
            "description",
            "start",
            "end"
        )

    def get_images(self, obj):
        images = obj.eventimages_set.all()
        return EventImageSerializer(images, many=True).data

    def get_start(self, obj):
        format = obj.start_date.strftime("%d %h %Y")
        return format

    def get_end(self, obj):
        format = obj.end_date.strftime("%d %h %Y")
        return format

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        other_events = Event.objects.exclude(id=instance.id).order_by("start_date")
        repr_["other events"] = EventListSerializer(other_events, many=True).data
        return repr_


