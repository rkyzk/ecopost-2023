"""This module holds tests for models."""

from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from sqlite3 import IntegrityError
from .models import Post, Comment


class TestPostModel(TestCase):

    def setUp(self):
        """create test users and posts"""
        self.user1 = User.objects.create(username="test1", password="password")
        self.user2 = User.objects.create(username="test2", password="password")
        self.post1 = Post.objects.create(
            title="title1",
            author=self.user1,
            content="test sentences"
            )
        self.post2 = Post.objects.create(
            title="title2",
            author=self.user2,
            content="test 2 sentences"
            )

    def test_featured_flag_default_to_False(self):
        self.assertEqual(self.post1.featured_flag, False)

    def test_featured_image_default_to_placeholder(self):
        self.assertEqual(self.post1.featured_image, 'placeholder')

    def test_category_default_to_Others(self):
        self.assertEqual(self.post1.category, 'others')

    def test_status_default_to_0(self):
        self.assertEqual(self.post1.status, 0)

    def test_posts_ordered_by_created_on_newest_to_oldest(self):
        posts = Post.objects.all()
        i = 0
        for i in range(len(posts) - 2):
            self.assertGreater(posts[i].created_on, posts[i+1].created_on)
            i += 1

    def test_post_will_be_slugified(self):
        self.assertTrue(self.post1.slug.startswith('title1'))

    def test_str_method_will_return_title(self):
        self.assertEqual(str(self.post1), 'title1')

    def test_pub_date_returns_string_message_if_not_published(self):
        self.assertEqual(self.post2.pub_date(), 'Not published')

    def test_pub_date_returns_specified_format_if_published(self):
        date = datetime.utcnow()
        self.post1.status = 2
        self.post1.published_on = date
        self.assertEqual(self.post1.pub_date(), date.strftime("%B %d, %Y"))

    def test_excerpt_returns_specified_str(self):
        content = "I'm writing a long content to test " + \
            "if the excerpt method returns the first 199 characters and " + \
            "... are returned. test test test test test sentences." + \
            "test sentences, test sentences, test sentences "
        post3 = Post.objects.create(
            title="title3",
            author=self.user1,
            content=content
        )
        self.assertEqual(post3.excerpt(), str(content)[0:199] + "...")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.post1.get_absolute_url(), '/detail/' + self.post1.slug + '/')


