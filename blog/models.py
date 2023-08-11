"""This module holds models used in ecopost."""

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Submitted"), (2, "Published"), (3, "Declined"))

CATEGORY = (('animals', 'protecting animals'),
            ('aquatic system', 'protecting the aquatic system'),
            ('saving soil & trees', 'protecting soil & trees'),
            ('saving resources', 'saving resources'),
            ('eco-conscious diet', 'eco-conscious diet'),
            ('others', 'others'))


class Post(models.Model):
    """Lists fields of Post model and functions around them."""
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    featured_flag = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image',
                                     default='placeholder',
                                     blank=True,
                                     transformation={
                                        'crop': 'fill_pad',
                                        'width': 510,
                                        'height': 340,
                                        'gravity': 'auto',
                                        'q_auto': 'good'
                                     })
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,
                                   related_name='post_likes',
                                   blank=True)
    num_of_likes = models.IntegerField(default=0)
    city = models.CharField(max_length=25)
    country = CountryField(max_length=25)
    category = models.CharField(max_length=30, choices=CATEGORY,
                                default='others')
    bookmark = models.ManyToManyField(User, related_name='bookmarked',
                                      blank=True)

    class Meta:
        ordering = ['-created_on', '-published_on']

    def __str__(self):
        """
        Returns the title.
        :return: title
        :rtype: str
        """
        return self.title
