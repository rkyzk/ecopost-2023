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
#     def test_get_postlist(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html', 'base.html')

#     def test_get_postlist_display_3_featured_stories(self):
#         response = self.client.get('/')
#         self.assertEqual(len(response.context['post_list']), 3)
#         self.assertEqual(list(response.context['post_list']),
#                          [self.post3, self.post2, self.post1])

# # Testing "AddStoryView" -----------------------------------------
#     def test_get_add_story_will_redirect_to_login_if_not_logged_in(self):
#         response = self.client.get(reverse('add_story'))
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(response.url.startswith('/accounts/login/'))

#     def test_can_get_add_story_if_logged_in(self):
#         response = self.c.get("/add_story/")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'base.html', 'add_story.html')

#     def test_add_story_POST_can_add_story(self):
#         response = self.c.post('/add_story/',
#                                {'title': 'test blog',
#                                 'content': 'test',
#                                 'city': 'test',
#                                 'country': 'IR',
#                                 'category': 'others',
#                                 'save': 'draft'})
#         post = Post.objects.filter(title='test blog').first()
#         self.assertEqual(post.title, 'test blog')
#         self.assertEqual(post.content, 'test')
#         self.assertRedirects(response, f'/detail/{post.slug}/')

#     def test_add_story_POST_will_set_status_to_1_if_submit_clicked(self):
#         response = self.c.post('/add_story/',
#                                {'title': 'test blog',
#                                 'content': 'test',
#                                 'city': 'test',
#                                 'country': 'IR',
#                                 'category': 'others',
#                                 'submit': 'complete'})
#         post = Post.objects.filter(title='test blog').first()
#         self.assertEqual(post.title, 'test blog')
#         self.assertEqual(post.status, 1)
#         self.assertRedirects(response, f'/detail/{post.slug}/')

#     def test_add_story_POST_keeps_status_to_0_if_save_clicked(self):
#         response = self.c.post('/add_story/',
#                                {'title': 'test blog',
#                                 'content': 'test',
#                                 'city': 'test',
#                                 'country': 'IR',
#                                 'category': 'others',
#                                 'save': 'draft'})
#         post = Post.objects.filter(title='test blog').first()
#         self.assertEqual(post.title, 'test blog')
#         self.assertEqual(post.status, 0)
#         self.assertRedirects(response, f'/detail/{post.slug}/')

#     def test_add_story_POST_save_will_render_msg_draft_saved(self):
#         response = self.c.post('/add_story/',
#                                {'title': 'test blog',
#                                 'content': 'test',
#                                 'city': 'test',
#                                 'country': 'IR',
#                                 'category': 'others',
#                                 'save': 'draft'})
#         messages = list(get_messages(response.wsgi_request))  
#         self.assertEqual(str(messages[0]), 'Your draft has been saved.')

#     def test_message_says_draft_is_submitted_if_submitted(self):
#         response = self.c.post('/add_story/',
#                                {'title': 'test blog',
#                                 'content': 'test',
#                                 'city': 'test',
#                                 'country': 'IR',
#                                 'category': 'others',
#                                 'submit': 'complete'})
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(str(messages[0]),
#                          "You submitted your post. We'll contact " +
#                          "you when decision has been made.")

# Testing "PostDetailView" -----------------------------------------
    # def test_can_get_detail_page(self):
    #     response = self.client.get(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html', 'base.html')

    # def test_post_detail_GET_liked_set_False_if_not_liked(self):
    #     response = self.c2.get(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.context['liked'], False)

    # def test_post_like_GET_will_set_liked_True_if_liked(self):
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     post.likes.add(self.user2)
    #     post.save()
    #     self.assertTrue(post.likes.filter(id=self.user2.id).exists())
    #     response = self.c2.get(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.context['liked'], True)

    # def test_post_detail_POST_liked_set_False_if_not_liked(self):
    #     response = self.c2.post(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.context['liked'], False)

    # def test_post_like_POST_will_set_liked_True_if_liked(self):
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     post.likes.add(self.user2)
    #     post.save()
    #     self.assertTrue(post.likes.filter(id=self.user2.id).exists())
    #     response = self.c2.post(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.context['liked'], True)

    # def test_post_detail_GET_bookmarked_set_False_if_not_bookmarked(self):
    #     response = self.c2.get(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.context['bookmarked'], False)

    # def test_post_detail_GET_will_set_bookmarked_True_if_bookmarked(self):
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     post.bookmark.add(self.user2)
    #     post.save()
    #     self.assertTrue(post.bookmark.filter(id=self.user2.id).exists())
    #     response = self.c2.get(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.context['bookmarked'], True)

    # def test_post_detail_POST_bookmarked_set_False_if_not_bookmarked(self):
    #     response = self.c2.post(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.context['bookmarked'], False)

    # def test_post_detail_POST_will_set_bookmarked_True_if_bookmarked(self):
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     post.bookmark.add(self.user2)
    #     post.save()
    #     self.assertTrue(post.bookmark.filter(id=self.user2.id).exists())
    #     response = self.c2.post(f'/detail/{self.post1.slug}/')
    #     self.assertEqual(response.context['bookmarked'], True)

    # def test_post_detail_POST_can_post_comment(self):
    #     response = self.c.post(f'/detail/{self.post1.slug}/',
    #                            {'body': 'test comment'})
    #     comment = Comment.objects.filter(commenter=self.user1).last()
    #     self.assertEqual(comment.body, 'test comment')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html', 'base.html')

    # def test_post_detail_POST_msg_says_comment_posted_if_submitted(self):
    #     response = self.c.post(f'/detail/{self.post1.slug}/',
    #                            {'body': 'test comment'})
    #     messages = list(response.context['messages'])
    #     self.assertEqual(str(messages[0]), 'You posted a comment.')

    # def test_post_detail_POST_error_message_if_a_space_entered(self):
    #     response = self.c.post(f'/detail/{self.post1.slug}/',
    #                            {'body': ' '})
    #     self.assertContains(response,
    #                         '<div class="alert alert-info alert-dismissible' +
    #                         ' fade show" id="msg" role="alert">',
    #                         status_code=200)
    #     self.assertContains(response,
    #                         'Error occurred. Your comment was not saved.',
    #                         status_code=200)

    # def test_detail_GET_shows_update_and_delete_btn_if_draft_and_author(self):
    #     self.post1.status = 0
    #     self.post1.save()
    #     response = self.c.get(f'/detail/{self.post1.slug}/')
    #     self.assertContains(response,
    #                         '<button class="button-submit"' +
    #                         ' name="update-post"' +
    #                         ' type="submit">update</button>',
    #                         status_code=200)
    #     self.assertContains(response,
    #                         '<button type="submit" class="button-submit"' +
    #                         ' name="delete_post" value="' +
    #                         self.post1.slug + '">delete</button>',
    #                         status_code=200)

    # def test_detail_GET_no_update_delete_btn_if_status1_and_author(self):
    #     self.post1.status = 1
    #     self.post1.save()
    #     response = self.c.get(f'/detail/{self.post1.slug}/')
    #     self.assertNotContains(response,
    #                            '<button class="button-submit"' +
    #                            ' name="update-post"' +
    #                            ' type="submit">update</button>',
    #                            status_code=200)
    #     self.assertNotContains(response,
    #                            '<button type="submit" class="button-submit"' +
    #                            ' name="delete_post" value="' +
    #                            self.post1.slug + '">delete</button>',
    #                            status_code=200)

    # def test_detail_GET_no_update_and_delete_btn_if_status2_and_author(self):
    #     self.post1.status = 2
    #     self.post1.save()
    #     response = self.c.get(f'/detail/{self.post1.slug}/')
    #     self.assertNotContains(response,
    #                            '<button class="button-submit"' +
    #                            ' name="update-post"' +
    #                            ' type="submit">update</button>',
    #                            status_code=200)
    #     self.assertNotContains(response,
    #                            '<button type="submit" class="button-submit"' +
    #                            ' name="delete_post" value="' +
    #                            self.post1.slug + '">delete</button>',
    #                            status_code=200)

    # def test_detail_GET_no_show_update_and_delete_btn_if_not_author(self):
    #     response = self.c2.get(f'/detail/{self.post1.slug}/')
    #     self.assertNotContains(response,
    #                            '<button class="button-submit"' +
    #                            ' name="update-post"' +
    #                            ' type="submit">update</button>',
    #                            status_code=200)
    #     self.assertNotContains(response,
    #                            '<button type="submit" class="button-submit"' +
    #                            ' name="delete_post" value="' +
    #                            self.post1.slug + '">delete</button>',
    #                            status_code=200)

    # Testing "PostLikeView" -----------------------------------------
    # def test_post_like_POST_will_add_user(self):
    #     response = self.c2.post(reverse('post_like',
    #                                     kwargs={'slug': self.post1.slug}))
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     self.assertRedirects(response, f'/detail/{self.post1.slug}/')
    #     self.assertTrue(post.likes.filter(id=self.user2.id).exists())

    # def test_post_like_POST_for_the_second_time_will_remove_user(self):
    #     response = self.c2.post(reverse('post_like',
    #                             kwargs={'slug': self.post1.slug}))
    #     response = self.c2.post(reverse('post_like',
    #                             kwargs={'slug': self.post1.slug}))
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     self.assertRedirects(response, f'/detail/{self.post1.slug}/')
    #     self.assertFalse(post.likes.filter(id=self.user2.id).exists())

# Testing "BookmarkView" -----------------------------------------
    # def test_bookmark_POST_will_add_user(self):
    #     response = self.c2.post(reverse('bookmark',
    #                                     kwargs={'slug': self.post1.slug}))
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     self.assertRedirects(response, f'/detail/{self.post1.slug}/')
    #     self.assertTrue(post.bookmark.filter(id=self.user2.id).exists())

    # def test_bookmark_POST_for_2nd_time_will_remove_user(self):
    #     response = self.c2.post(reverse('bookmark',
    #                                     kwargs={'slug': self.post1.slug}))
    #     response = self.c2.post(reverse('bookmark',
    #                                     kwargs={'slug': self.post1.slug}))
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     self.assertRedirects(response, f'/detail/{self.post1.slug}/')
    #     self.assertFalse(post.bookmark.filter(id=self.user2.id).exists())

    # Testing "UpdateCommentView" -----------------------------------------
    # def test_update_comment_GET_gets_the_page_if_right_user(self):
    #     response = self.c.get('/update_comment/comment1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'update_comment.html', 'base.html')

    # def test_update_comment_GET_will_redirect_to_login_if_not_logged_in(self):
    #     response = self.client.get('/update_comment/comment1/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(response.url.startswith('/accounts/login/'))

    # def test_update_comment_GET_will_403_if_wrong_user(self):
    #     response = self.c2.get(reverse('update_comment', kwargs={'id': 1}))
    #     self.assertEqual(response.status_code, 403)

    # def test_update_comment_POST_will_update_comment(self):
    #     response = self.c.post('/update_comment/comment1/',
    #                            {'body': 'comment updated'})
    #     comment = Comment.objects.filter(commenter=self.user1).first()
    #     self.assertEqual(comment.body, 'comment updated')
    #     self.assertEqual(comment.comment_status, 1)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, f'/detail/{comment.post.slug}/')

    # Testing "DeleteCommentView" -----------------------------------------
    # def test_delete_comment_POST_will_set_comment_status_to_2(self):
    #     response = self.c.post('/delete_comment/comment1/')
    #     comment = Comment.objects.filter(commenter=self.user1).first()
    #     self.assertEqual(comment.comment_status, 2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, f'/detail/{comment.post.slug}/')

    # Testing "UpdatePostView" -----------------------------------------
    # def test_update_post_GET_gets_the_page_if_right_user(self):
    #     response = self.c.get(f'/update/{self.post6.slug}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'update_post.html', 'base.html')

    # def test_update_post_GET_will_redirect_to_login_if_not_logged_in(self):
    #     response = self.client.get(f'/update/{self.post1.slug}/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(response.url.startswith('/accounts/login/'))

    # def test_update_post_GET_will_403_if_wrong_user(self):
    #     response = self.c2.get(f'/update/{self.post1.slug}/')
    #     self.assertEqual(response.status_code, 403)

    # def test_update_post_GET_will_403_if_submitted(self):
    #     self.post1.status = 1
    #     self.post1.save()
    #     response = self.c.get(f'/update/{self.post1.slug}/')
    #     self.assertEqual(response.status_code, 403)

    # def test_update_post_GET_will_403_if_published(self):
    #     self.post1.status = 2
    #     self.post1.save()
    #     response = self.c.get(f'/update/{self.post1.slug}/')
    #     self.assertEqual(response.status_code, 403)

    # def test_update_post_POST_will_update_title(self):
    #     response = self.c.post(reverse('update_post',
    #                            kwargs={'slug': self.post6.slug}),
    #                            {'title': 'title updated',
    #                             'content': 'content',
    #                             'city': 'test city',
    #                             'country': 'IR',
    #                             'category': 'others',
    #                             'save': 'draft'})
    #     post = Post.objects.filter(slug=self.post6.slug).first()
    #     self.assertEqual(post.title, 'title updated')
    #     self.assertEqual(post.content, 'content')
    #     self.assertEqual(post.city, 'test city')
    #     self.assertEqual(post.country, 'IR')
    #     self.assertEqual(post.category, 'others')
    #     self.assertRedirects(response, f'/detail/{post.slug}/')

    # def test_update_post_POST_will_update_content(self):
    #     response = self.c.post(reverse('update_post',
    #                            kwargs={'slug': self.post6.slug}),
    #                            {'title': 'title6',
    #                             'content': 'content updated',
    #                             'city': 'test city',
    #                             'country': 'IR',
    #                             'category': 'others',
    #                             'save': 'draft'})
    #     post = Post.objects.filter(slug=self.post6.slug).first()
    #     self.assertEqual(post.title, 'title6')
    #     self.assertEqual(post.content, 'content updated')
    #     self.assertEqual(post.city, 'test city')
    #     self.assertEqual(post.country, 'IR')
    #     self.assertEqual(post.category, 'others')
    #     self.assertRedirects(response, f'/detail/{post.slug}/')

    # def test_update_post_POST_will_update_city(self):
    #     response = self.c.post(reverse('update_post',
    #                            kwargs={'slug': self.post6.slug}),
    #                            {'title': 'title6',
    #                             'content': 'content',
    #                             'city': 'test city 2',
    #                             'country': 'IR',
    #                             'category': 'others',
    #                             'save': 'draft'})
    #     post = Post.objects.filter(slug=self.post6.slug).first()
    #     self.assertEqual(post.title, 'title6')
    #     self.assertEqual(post.content, 'content')
    #     self.assertEqual(post.city, 'test city 2')
    #     self.assertEqual(post.country, 'IR')
    #     self.assertEqual(post.category, 'others')
    #     self.assertRedirects(response, f'/detail/{post.slug}/')

    # def test_update_post_POST_will_update_country(self):
    #     response = self.c.post(reverse('update_post',
    #                            kwargs={'slug': self.post6.slug}),
    #                            {'title': 'title6',
    #                             'content': 'content',
    #                             'city': 'test city',
    #                             'country': 'NZ',
    #                             'category': 'others',
    #                             'save': 'draft'})
    #     post = Post.objects.filter(slug=self.post6.slug).first()
    #     self.assertEqual(post.title, 'title6')
    #     self.assertEqual(post.content, 'content')
    #     self.assertEqual(post.city, 'test city')
    #     self.assertEqual(post.country, 'NZ')
    #     self.assertEqual(post.category, 'others')
    #     self.assertRedirects(response, f'/detail/{post.slug}/')

    # def test_update_post_POST_will_update_category(self):
    #     response = self.c.post(reverse('update_post',
    #                            kwargs={'slug': self.post6.slug}),
    #                            {'title': 'title6',
    #                             'content': 'content',
    #                             'city': 'test city',
    #                             'country': 'IR',
    #                             'category': 'aquatic system',
    #                             'save': 'draft'})
    #     post = Post.objects.filter(slug=self.post6.slug).first()
    #     self.assertEqual(post.title, 'title6')
    #     self.assertEqual(post.content, 'content')
    #     self.assertEqual(post.city, 'test city')
    #     self.assertEqual(post.country, 'IR')
    #     self.assertEqual(post.category, 'aquatic system')
    #     self.assertRedirects(response, f'/detail/{post.slug}/')

    # def test_update_post_POST_cancel_will_not_update_post(self):
    #     response = self.c.post(reverse('update_post',
    #                                    kwargs={'slug': self.post6.slug}),
    #                            {'title': 'title6',
    #                             'content': 'content updated',
    #                             'city': 'test city',
    #                             'country': 'IR',
    #                             'category': 'others',
    #                             'cancel': 'cancel'})
    #     post = Post.objects.filter(slug=self.post6.slug).first()
    #     self.assertEqual(post.title, 'title6')
    #     self.assertEqual(post.content, 'content updated')
    #     self.assertEqual(post.city, 'test city')
    #     self.assertEqual(post.country, 'IR')
    #     self.assertEqual(post.category, 'others')
    #     self.assertRedirects(response, f'/detail/{post.slug}/')

    # def test_update_post_POST_msg_says_change_saved_if_saved(self):
    #     response = self.c.post(reverse('update_post',
    #                            kwargs={'slug': self.post6.slug}),
    #                            {'title': 'title6',
    #                             'content': 'content updated',
    #                             'city': 'test city',
    #                             'country': 'IR',
    #                             'category': 'others',
    #                             'save': 'draft'},
    #                            follow=True)
    #     messages = list(response.context['messages'])
    #     self.assertEqual(str(messages[0]), "The change has been saved.")

    # def test_update_post_POST_submit_will_set_status_to_1(self):
    #     response = self.c.post(reverse('update_post',
    #                                    kwargs={'slug': self.post6.slug}),
    #                            {'title': 'title6',
    #                             'content': 'content updated',
    #                             'city': 'test city',
    #                             'country': 'IR',
    #                             'category': 'others',
    #                             'submit': 'complete'})
    #     post = Post.objects.filter(slug=self.post6.slug).first()
    #     self.assertEqual(post.status, 1)

    # Testing "DeletePostView" ----------------------------------
    # def test_delete_post_POST_will_delete_post_if_right_user(self):
    #     response = self.c.post(reverse('delete_post',
    #                                    kwargs={'slug': self.post6.slug}))
    #     existing_posts = Post.objects.filter(slug=self.post6.slug)
    #     self.assertEqual(len(existing_posts), 0)
    #     self.assertRedirects(response, '/')

    # def test_delete_post_POST_will_show_403_if_wrong_user(self):
    #     response = self.c2.post(reverse('delete_post',
    #                                     kwargs={'slug': self.post6.slug}))
    #     self.assertEqual(response.status_code, 403)

    # def test_delete_post_POST_will_not_delete_post_if_wrong_user(self):
    #     response = self.c2.post(reverse('delete_post',
    #                                     kwargs={'slug': self.post6.slug}))
    #     post = Post.objects.filter(slug=self.post1.slug).first()
    #     self.assertEqual(post.title, 'title1')

    # def test_delete_post_POST_will_show_403_if_status_1(self):
    #     self.post1.status = 1
    #     self.post1.save()
    #     response = self.c2.post(reverse('delete_post',
    #                                     kwargs={'slug': self.post1.slug}))
    #     self.assertEqual(response.status_code, 403)

    # def test_delete_post_POST_will_show_403_if_status_2(self):
    #     self.post1.status = 2
    #     self.post1.save()
    #     response = self.c2.post(reverse('delete_post',
    #                                     kwargs={'slug': self.post1.slug}))
    #     self.assertEqual(response.status_code, 403)

    # Testing "MoreStoriesView" ----------------------------------
    # def test_can_get_more_stories(self):
    #     response = self.client.get('/more_stories/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'more_stories.html')

    # def test_more_stories_display_posts_published_in_the_prev_7_days(self):
    #     self.post4.published_on = datetime.utcnow() - timedelta(days=10)
    #     self.post4.save()
    #     response = self.client.get('/more_stories/')
    #     self.assertEqual(len(response.context['object_list']), 1)
    #     self.assertEqual(list(response.context['object_list']),
    #                      [self.post5])

    # Testing "PopularStoriesView" ----------------------------------
    # def test_can_get_readers_favorite_stories(self):
    #     response = self.client.get('/popular_stories/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'popular_stories.html')

    # def test_favorite_stories_display_right_posts(self):
    #     self.post4.likes.add(self.user1)
    #     self.post4.save()
    #     response = self.client.get('/popular_stories/')
    #     self.assertEqual(len(response.context['object_list']), 1)
    #     self.assertEqual(list(response.context['object_list']),
    #                      [self.post4])

    # Testing "MyPageView" ----------------------------------
    # def test_my_page_GET_will_get_page_if_user(self):
    #     response = self.c.get('/my_page/' + str(self.user1.id) + '/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'my_page.html', 'base.html')

    # def test_my_page_GET_will_403_if_wrong_user(self):
    #     response = self.c2.get('/my_page/' + str(self.user1.id) + '/')
    #     self.assertEqual(response.status_code, 403)
