# Generated by Django 3.2.20 on 2023-08-11 04:56

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('featured_flag', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('published_on', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Submitted'), (2, 'Published'), (3, 'Declined')], default=0)),
                ('num_of_likes', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=25)),
                ('category', models.CharField(choices=[('animals', 'protecting animals'), ('aquatic system', 'protecting the aquatic system'), ('saving soil & trees', 'protecting soil & trees'), ('saving resources', 'saving resources'), ('eco-conscious diet', 'eco-conscious diet'), ('others', 'others')], default='others', max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('bookmark', models.ManyToManyField(blank=True, related_name='bookmarked', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on', '-published_on'],
            },
        ),
    ]
