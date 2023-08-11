from django.contrib import admin
from django.db import models
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Customizes the appearance of Post model on the admin panel."""
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'published_on')
