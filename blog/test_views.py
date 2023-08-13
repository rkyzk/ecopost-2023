"""This module holds tests for views."""

from django.test import TestCase, Client
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404
from django.contrib.messages import get_messages
from django.core.exceptions import PermissionDenied
from datetime import datetime, timedelta


class TestViews(TestCase):

    def setUp(self):
        """Creates test users and posts.  Logs in the test users."""
        self.user1 = User.objects.create_user(username="user1")
        self.user1.set_password('password')
        self.user1.save()
        self.c = Client()
        logged_in = self.c.login(username='user1', password='password')
        self.user2 = User.objects.create_user(username="user2")
        self.user2.set_password('pw2')
        self.user2.save()
        self.c2 = Client()
        logged_in = self.c2.login(username='user2', password='pw2')
        self.post1 = Post.objects.create(title='title1',
                                         author=self.user1,
                                         content='content',
                                         city='Dublin',
                                         country='IR',
                                         status=2,
                                         featured_flag=True,
                                         category='Others')
        self.post2 = Post.objects.create(title='title2',
                                         author=self.user1,
                                         content='content',
                                         city='Dublin',
                                         country='IR',
                                         status=2,
                                         featured_flag=True,
                                         category='Others')
        self.post3 = Post.objects.create(title='title3',
                                         author=self.user1,
                                         content='content',
                                         city='Dublin',
                                         country='IR',
                                         status=2,
                                         featured_flag=True,
                                         category='others')
        self.post4 = Post.objects.create(title='title4',
                                         author=self.user1,
                                         content='content',
                                         city='Dublin',
                                         country='IR',
                                         status=2,
                                         category='Others')
        self.post5 = Post.objects.create(title='title5',
                                         author=self.user1,
                                         content='content',
                                         city='Dublin',
                                         country='IR',
                                         status=2,
                                         category='Others')
        self.post6 = Post.objects.create(title='title6',
                                         author=self.user1,
                                         content='content',
                                         city='Dublin',
                                         country='IR',
                                         status=0,
                                         category='Others')
        self.comment1 = Comment.objects.create(body='test comment',
                                               commenter=self.user1,
                                               post=self.post1)

    # Testing "PostListView" -----------------------------------------
    def test_get_postlist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_get_postlist_display_3_featured_stories(self):
        response = self.client.get('/')
        self.assertEqual(len(response.context['post_list']), 3)
        self.assertEqual(list(response.context['post_list']),
                         [self.post3, self.post2, self.post1])
