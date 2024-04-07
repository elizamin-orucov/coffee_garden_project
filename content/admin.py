from django.contrib import admin
from .models import News, NewsImage
from modeltranslation.admin import TranslationAdmin


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_filter = ("title", "created_at")
    inlines = (NewsImageInline,)


admin.site.register(News, NewsAdmin)

