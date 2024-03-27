from django.db import models
from store.models import Product
from services.mixin import DateMixin
from django.contrib.auth import get_user_model


Users = get_user_model()


class Basket(DateMixin):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "product"
        verbose_name_plural = "Baskets"
