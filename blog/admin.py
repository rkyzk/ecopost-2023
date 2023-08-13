from django.contrib import admin
from django.db import models
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Customizes the appearance of Post model on the admin panel."""
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status', 'published_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Customizes the appearance of Comment model on the admin panel."""
    list_display = ('commenter', 'body', 'post',
                    'created_on', 'comment_status')
    list_filter = ('created_on', 'comment_status')
    search_fields = ('commenter', 'body')
