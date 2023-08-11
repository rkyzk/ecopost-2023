from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    """Gets queryset of featured posts and displays them on the home page."""
    model = Post
    queryset = Post.objects.filter(featured_flag=True).order_by(
        "-created_on")[:3]
    template_name = "index.html"


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
            # Stores in post attribute of comment,
            # to which post this comment belongs.
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



