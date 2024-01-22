# Generated by Django 3.2 on 2024-01-22 19:41

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import services.uploader


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('code', models.SlugField(editable=False, unique=True)),
                ('title', models.CharField(max_length=350)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.news_image_uploader)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.news')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'News Images',
            },
        ),
    ]
