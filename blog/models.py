"""This module holds models used in ecopost."""

import random
import string
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField
from django.shortcuts import reverse
from datetime import datetime


STATUS = ((0, "Draft"), (1, "Submitted"), (2, "Published"), (3, "Declined"))

COMMENT_STATUS = ((0, "original"), (1, "edited"), (2, "deleted"))

CATEGORY = (('animals', 'protecting animals'),
            ('aquatic system', 'protecting the aquatic system'),
            ('saving soil & trees', 'protecting soil & trees'),
            ('saving resources', 'saving resources'),
            ('eco-conscious diet', 'eco-conscious diet'),
            ('others', 'others'))


class Post(models.Model):
    """Lists fields of Post model and functions around them."""
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True, editable=False)
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

    def save(self, *args, **kwargs):
        """
        As the post is saved for the first time, assign a slug.
        If the status is 'Published,' but the published date
        hasn't been recorded, assign the current date and time.
        Save likes count.
        """
        if not self.slug:
            # add a random string after the title
            random_str = ''.join(random.choices(string.ascii_letters +
                                 string.digits, k=16))
            self.slug = slugify(self.title + '-' + random_str)
        # if the post has been published but published_on is empty
        # assign the current datetime.
        if self.status == 2 and not self.published_on:
            self.published_on = datetime.utcnow()
        # save number of likes
        if self.id is not None:
            self.num_of_likes = self.likes.count()
        super().save(*args, **kwargs)

    def excerpt(self):
        """
        Returns the first 200 letters of the post.
        :returns: excerpt
        :rtype: str
        """
        excerpt = str(self.content)[0:199] + "..."
        return excerpt

    def pub_date(self):
        """
        Returns the published date.
        If the post hasn't been published, return 'Not published.'
        :returns: published_on or 'Not published'
        :rtype: str
        """
        if self.status == 2:
            return self.published_on.strftime("%B %d, %Y")
        else:
            return 'Not published'

    def get_absolute_url(self):
        """
        Returns the URL of 'Detail Page.'
        :return: reverse
        """
        return reverse('detail_page', kwargs={'slug': self.slug})


class Comment(models.Model):
    """Lists fields of Comment model and the functions around them."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='commenter')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment_status = models.IntegerField(choices=COMMENT_STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        """
        Returns the comment body and the commenter.
        :return: comment and the commenter in string
        :rtype: str
        """
        return f"{self.body} by {self.commenter.username}"
