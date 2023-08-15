import django_filters
from .models import Post, CATEGORY
from django_countries.fields import CountryField
from django.db.models import Q


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author__username = django_filters.CharFilter(lookup_expr='icontains',
                                                 label='Author')
    published_after = django_filters.DateFilter(method='filter_start_date',
                                                label='published_after')
    published_before = django_filters.DateFilter(method='filter_end_date',
                                                 label='published_before')
    num_of_likes = django_filters.NumberFilter(method='filter_likes',
                                               label='liked more than')
    category = django_filters.ChoiceFilter(choices=CATEGORY)
    city = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.ChoiceFilter(choices=CountryField().get_choices())
    search_keyword = django_filters.CharFilter(method='filter_keyward',
                                               label='keyword')

    class Meta:
        model = Post
        fields = ['title', 'author__username', 'content', 'published_on',
                  'num_of_likes', 'category', 'city', 'country']

    def filter_keyword(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) |
                               Q(content__icontains=value))

    def filter_likes(self, queryset, name, value):
        return queryset.filter(Q(num_of_likes__gte=value))

    def filter_start_date(self, queryset, name, value):
        return queryset.filter(Q(published_on__gte=value))

    def filter_end_date(self, queryset, name, value):
        return queryset.filter(Q(published_on__lte=value))
