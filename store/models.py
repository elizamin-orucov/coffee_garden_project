from django.db import models
from base.models import Category
from services.slugify import slugify
from services.uploader import Uploader
from ckeditor.fields import RichTextField
from services.generator import CodeGenerator
from django.contrib.auth import get_user_model
from services.mixin import SlugMixin, DateMixin
from services.choices import PRODUCT_STATUS_CHOICES, DISCOUNT_CHOICES


User = get_user_model()


class Product(SlugMixin):
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField()
    size = models.CharField(max_length=150, blank=True, null=True)
    discount_interest = models.IntegerField(blank=True, null=True, choices=DISCOUNT_CHOICES)
    status = models.CharField(max_length=50, choices=PRODUCT_STATUS_CHOICES)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        discount_price = self.price * (self.discount_interest or 0) / 100
        discounted_price = self.price - discount_price
        return round(float(discounted_price), 2)

    def create_unique_slug(self, slug, index=0):
        new_slug = slug
        if index:
            new_slug = f"{slug}-{index}"
        qs = self.__class__.objects.filter(slug=new_slug)
        return self.create_unique_slug(slug, index+1) if qs.exists() else new_slug

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = CodeGenerator.create_product_shortcode(
                size=5, model_=self.__class__
            )
        if not self.slug:
            self.slug = self.create_unique_slug(slugify(title=self.name))
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Produktlar"
        verbose_name = "Produkt"


class ProductImages(DateMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=Uploader.product_image_uploader)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = "Produkt şəkilləri"
        verbose_name = "Şəkil"


class Coupon(DateMixin):
    user = models.ManyToManyField(User, blank=True)
    code = models.CharField(max_length=30)
    discount_rate = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"


