from django.contrib import admin
from .models import Order, OrderItem, TrackOrder, ShippingMethod


class ItemsInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ("invoice_id", "email", "billing_status")
    inlines = (ItemsInline,)


admin.site.register(Order, OrderAdmin)
admin.site.register(TrackOrder)
admin.site.register(ShippingMethod)


