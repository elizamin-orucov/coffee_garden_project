from rest_framework import generics
from ..models import ContactUs, Subscriber, AboutUs, OurLocation
from .serializer import (
    ContactUsSerializer, SubscriberSerializer,
    AboutUsSerializer, OurLocationSerializer
)


class ContactUsView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class SubscriberView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class AboutUsView(generics.RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get_object(self):
        return self.queryset.first()


class OurLocationView(generics.RetrieveAPIView):
    queryset = OurLocation.objects.all()
    serializer_class = OurLocationSerializer

    def get_object(self):
        return self.queryset.first()





