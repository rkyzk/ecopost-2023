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
