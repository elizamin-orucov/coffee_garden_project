from django.db import models
from services.mixin import DateMixin
from store.models import Coupon, Product
from services.generator import CodeGenerator
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from services.choices import TRACK_ORDER_STATUS, ORDER_STATUS_CHOICES


User = get_user_model()


class Order(DateMixin):
    invoice_id = models.PositiveIntegerField(unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_order")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=270, blank=True)
    address = models.CharField(max_length=300)
    country = CountryField()
    city = models.CharField(max_length=150)
    phone = PhoneNumberField()
    postal_code = models.PositiveIntegerField()
    coupon_discount = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True, related_name="coupon")
    shipping_method = models.ForeignKey("order.ShippingMethod", on_delete=models.SET_NULL, null=True)
    subtotal = models.FloatField(null=True)
    total_paid = models.FloatField()
    billing_status = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, null=True)

    def __str__(self):
        return str(self.invoice_id)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            self.invoice_id = int(CodeGenerator.create_invoice_id(size=8, model_=self.__class__))
        return super().save(*args, **kwargs)


class OrderItem(DateMixin):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"


class TrackOrder(DateMixin):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=70, choices=TRACK_ORDER_STATUS, default="Sender is preparing to ship your order")

    def __str__(self):
        return self.order.user.email


class ShippingMethod(DateMixin):
    method = models.CharField(max_length=100)
    duration = models.CharField(max_length=150)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.method

    class Meta:
        verbose_name = "method"
        verbose_name_plural = "Shipping methods"


