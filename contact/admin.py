from django.contrib import admin
from .models import ContactUs, AboutUs, OurLocation, Subscriber


admin.site.register(ContactUs)
admin.site.register(AboutUs)
admin.site.register(Subscriber)
admin.site.register(OurLocation)
