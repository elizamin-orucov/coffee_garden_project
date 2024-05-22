# Generated by Django 5.0.6 on 2024-05-22 22:05

import ckeditor.fields
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300)),
                ('about', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='OurLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=300)),
                ('service', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('working_hours', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Our Location',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'email',
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=30)),
                ('subjects', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('message', models.TextField(max_length=500)),
                ('responsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
