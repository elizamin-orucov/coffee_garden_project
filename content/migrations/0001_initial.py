# Generated by Django 5.0.6 on 2024-05-22 22:05

import ckeditor.fields
import django.db.models.deletion
import services.uploader
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('code', models.SlugField(editable=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Active', 'Active'), ('Closed', 'Closed')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
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
                'verbose_name': 'content',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='EventImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.event_image_uploader)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.event')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'Event images',
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
                'verbose_name': 'image',
                'verbose_name_plural': 'News Images',
            },
        ),
    ]
