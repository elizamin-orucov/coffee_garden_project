from django.db import models
from store.models import Product
from services.mixin import DateMixin
from django.contrib.auth import get_user_model

User = get_user_model()


class WishList(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "Wishlist"

