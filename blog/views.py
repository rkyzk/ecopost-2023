from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .models import Post, Comment, Photo
from datetime import datetime, timedelta
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    """Gets queryset of featured posts and displays them on the home page."""
    model = Post
    queryset = Post.objects.filter(featured_flag=True).order_by(
        "-created_on")[:3]
    template_name = "index.html"


class AddStory(LoginRequiredMixin, generic.CreateView):
    """
    Display a post form on 'add_story' page for users
    to make a new post object.
    """
    model = Post
    template_name = "add_story.html"
    form_class = PostForm

    def form_valid(self, form):
        """
        Validates the form.
        arguments: self, form: Post form
        :return: super()
        :rtype: method
        """
        form.instance.author = self.request.user
        message = 'Your draft has been saved.'
        # If submitted, set the status to 1 ('Submitted.')
        if 'submit' in self.request.POST.keys():
            form.instance.status = 1
            message = "You submitted your post. " + \
                      "We'll contact you when decision has been made."
        form.save()
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(AddStory, self).form_valid(form)


class PostDetail(View):
    """
    Displays the full content of a post and the comments on 'post detail' page.
    Displays a comment form for users to leave comments.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        renders 'post detail' page.
        argument: self, request, slug
        :return: render()
        :rtype: method
        """
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('created_on')
        # If the user has liked the post, set 'liked' True
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # If the user has bookmarked the post, set 'bookmarked' True
        bookmarked = False
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "bookmarked": bookmarked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Receives posted comment form and validates it.
        If validated, saves it and displays the comment.
        If not, displays an error message and an empty comment form.
        arguments: self, request, slug, *args, **kwargs
        :return: render()
        :rtype: method
        """
        post = Post.objects.filter(slug=slug)[0]
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        bookmarked = False
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True
        # gets input data from the user and stores it in 'comment_form'
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.commenter = request.user
            comment = comment_form.save(commit=False)
            # record which post this comment belongs to.
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'You posted a comment.')
        else:
            comment_form = CommentForm()
            messages.add_message(request, messages.INFO, "Error occurred." +
                                 " Your comment was not saved.")
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "bookmarked": bookmarked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """Add or remove user in the foreign key likes of the post."""

    def post(self, request, slug, *args, **kwargs):
        """
        If user exists in 'likes' of the post, removes him/her.
        If not, add the user to 'likes.'
        arguments: self, request, slug, *args, **kwargs
        :return: HttpResponseRedirect
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        post.save()
        return HttpResponseRedirect(reverse('detail_page', args=[slug]))


class Bookmark(View):
    """Add or remove user to/from the foreign key 'bookmark' of the post."""

    def post(self, request, slug, *args, **kwargs):
        """
        If user exists in 'bookmark,' removes him/her.
        If not, add the user to 'bookmark.'
        arguments: self, request, slug, *args, **kwargs
        :return: HttpResponseRedirect()
        :rtype: method
        """
        post = get_object_or_404(Post, slug=slug)
        if post.bookmark.filter(id=request.user.id).exists():
            post.bookmark.remove(request.user)
        else:
            post.bookmark.add(request.user)
        return HttpResponseRedirect(reverse('detail_page', args=[slug]))


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """Update post."""
    model = Post
    template_name = "update_post.html"
    form_class = PostForm

    def form_valid(self, form):
        """
        validate the form and save it.
        arguments: self, form
        :return: super()
        :rtype: method
        """
        form.instance.author = self.request.user
        message = 'The change has been saved.'
        # If the post is submitted, set status to 1 ('Submitted')
        if 'submit' in self.request.POST.keys():
            form.instance.status = 1
            message = "You submitted your post. " + \
                      "We'll contact you when decision has been made."
        form.save()
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(UpdatePost, self).form_valid(form)

    def test_func(self):
        """
        test if status of the post is 0 ('draft')
        and user is the author of the post.
        :return: True/False
        :rtype: boolean
        """
        slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug=slug)
        return post.status == 0 and post.author == self.request.user


class DeletePost(LoginRequiredMixin, View):
    """Deletes posts."""

    def post(self, request, slug, *args, **kwargs):
        """
        Delete post and redirect to 'home.'
        arguments: self, request, slug, *args. **kwargs
        :returns: HttpResponseRedirect()
        :rtype: method
        """
        post = get_object_or_404(Post, slug=slug)
        if post.author == self.request.user and post.status == 0:
            post.delete()
            message = 'Your draft has been deleted.'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse('home'))
        else:
            raise PermissionDenied()


class UpdateComment(LoginRequiredMixin, UserPassesTestMixin, View):
    """Updates comments."""

    def get(self, request, id, *args, **kwargs):
        """
        Get comment from the DB,
        store it in comment form and display the update form
        for users to update the body.
        arguments: self, request, id: comment id, *args, **kwargs
        :returns: render()
        :rtype: method
        """
        comment = get_object_or_404(Comment, id=id)
        comment_form = CommentForm(instance=comment)
        return render(
            request,
            "update_comment.html",
            {
                "comment_form": comment_form,
                "slug": comment.post.slug
            }
        )

    def post(self, request, id, *args, **kwargs):
        """
        Receive comment form, validate it.
        If it's valid, update the comment.
        If not, store an error message. Redirect to "Detail Page."
        arguments: id: comment id
        :returns: HttpResponseRedirect()
        :rtype: method
        """
        comment = get_object_or_404(Comment, id=id)
        slug = comment.post.slug
        comment_form = CommentForm(self.request.POST, instance=comment)
        if comment_form.is_valid():
            updated = comment_form.save(commit=False)
            updated.commneter = request.user
            updated.comment_status = 1
            updated.save()
        else:
            comment_form = CommentForm()
            messages.add_message(request, messages.INFO, "Error occurred." +
                                 " Your comment was not saved.")
        return HttpResponseRedirect(reverse('detail_page', args=[slug]))

    def test_func(self):
        """
        Tests if the user has written the comment.
        :returns: True/False
        :rtype: boolean
        """
        id = self.kwargs.get('id')
        comment = get_object_or_404(Comment, id=id)
        return comment.commenter == self.request.user


class MyPage(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, pk, *args, **kwargs):
        """
        Make lists of 1) the posts written by the user,
        2) posts commented by the user
        3) posts bookmarked by the user,
        send the three lists to 'My page'
        arguments: self, request, pk: pk of the user, *args, **kwargs
        :returns: render()
        :rtype: method
        """
        my_posts = Post.objects.filter(author=pk)
        # Make a list of posts commented by the user
        comments = Comment.objects.filter(commenter__id=pk,
                                          comment_status__in=[0, 1])
        commented_posts = [comment.post for comment in comments]
        # remove duplicates
        commented_posts = list(dict.fromkeys(commented_posts))
        # Make a list of posts bookmarked by the user
        bookmarked_posts = Post.objects.filter(bookmark__in=[request.user.id])

        return render(
            request,
            "my_page.html",
            {
                "my_posts": my_posts,
                "commented_posts": commented_posts,
                "bookmarked_posts": bookmarked_posts
            },
        )

    def test_func(self):
        """
        Tests if the user is the owner of 'My Page'
        :returns: True/False
        :rtype: boolean
        """
        return self.kwargs.get('pk') == self.request.user.pk


class MoreStories(generic.ListView):
    """
    Get posts published in the past 7 days from DB,
    send the queryset and display 'More Stories' page.
    """
    model = Post
    template_name = "more_stories.html"
    paginate_by = 6
    filterargs = {
            'status': 2,
            'published_on__date__gte': datetime.utcnow() - timedelta(days=7),
            'featured_flag': False
            }
    queryset = Post.objects.filter(**filterargs).order_by("-published_on")
