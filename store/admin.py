from django.contrib import admin
from .models import Product, ProductImages


class ImageInline(admin.TabularInline):
    model = ProductImages
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "total_price")
    list_display_links = list_display
    inlines = (ImageInline, )


admin.site.register(Product, ProductAdmin)


