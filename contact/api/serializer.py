import phonenumbers
from rest_framework import serializers
from ..models import ContactUs, Subscriber, OurLocation, AboutUs


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            "full_name",
            "subjects",
            "email",
            "message",
        )


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = (
            "email",
        )

    def validate(self, attrs):
        email = attrs.get("email")

        # to prevent the same email from being re-registered
        if Subscriber.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "This email is now available."})

        return super().validate(attrs)


class OurLocationSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OurLocation
        fields = (
            "location",
            "phone_number",
            "working_hours"
        )

    def get_phone_number(self, obj):
        number = phonenumbers.format_number(obj.service, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        return number


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            "title",
            "about"
        )



