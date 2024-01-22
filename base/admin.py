from django.contrib import admin
from .models import Category
from modeltranslation.admin import TranslationAdmin

admin.site.register(Category)
