from django.db import models
from services.mixin import DateMixin
from mptt.models import MPTTModel, TreeForeignKey


class Category(DateMixin, MPTTModel):
    name = models.CharField(max_length=150)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
