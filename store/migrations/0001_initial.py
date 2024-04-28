# Generated by Django 3.2 on 2024-04-18 18:43

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import services.uploader


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('code', models.SlugField(editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('discount_interest', models.IntegerField(blank=True, choices=[(5, '5% off'), (10, '10% off'), (15, '15% off'), (20, '20% off'), (25, '25% off'), (30, '30% off'), (40, '40% off'), (50, '50% off'), (60, '60% off'), (70, '70% off')], null=True)),
                ('status', models.CharField(choices=[('Available Buy at Website', 'Available Buy at Website'), ('Available Only at Cafe', 'Available Only at Cafe')], max_length=50)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('images', models.ImageField(upload_to=services.uploader.Uploader.product_image_uploader)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'Product images',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=30)),
                ('discount_rate', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
                'ordering': ('-created_at',),
            },
        ),
    ]
