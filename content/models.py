from django.db import models
from services.slugify import slugify
from services.uploader import Uploader
from ckeditor.fields import RichTextField
from services.generator import CodeGenerator
from services.mixin import SlugMixin, DateMixin


class News(SlugMixin):
    title = models.CharField(max_length=350)
    content = RichTextField()

    def __str__(self):
        return self.title

    def create_unique_slug(self, slug, index=0):
        new_slug = slug
        if index:
            new_slug = f"{slug}-{index}"
        qs = self.__class__.objects.filter(slug=new_slug)
        return self.create_unique_slug(slug, index+1) if qs.exists() else new_slug

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = CodeGenerator.create_product_shortcode(
                size=8, model_=self.__class__
            )
        if not self.slug:
            self.slug = self.create_unique_slug(slugify(title=self.title))
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "News"


class NewsImage(DateMixin):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.news_image_uploader)

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "News Images"



