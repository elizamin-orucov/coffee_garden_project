from django.contrib import admin
from .models import News, NewsImage, Event, EventImages
from modeltranslation.admin import TranslationAdmin


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_filter = ("title", "created_at")
    inlines = (NewsImageInline,)


class EventImageInline(admin.TabularInline):
    model = EventImages
    extra = 1


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date")
    list_filter = ("start_date", "end_date")
    search_fields = ("title",)
    inlines = (EventImageInline,)


admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)

