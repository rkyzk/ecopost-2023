import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    class Meta:
        model: Post
        fields: ['title', 'author__username', 'content', 'published_on',
                 'num_of_likes', 'category', 'city', 'country']
