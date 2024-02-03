from django.contrib import admin
from .models import Order, OrderItem, TrackOrder, ShippingMethod


class ItemsInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ("invoice_id", )


admin.site.register(Order)


