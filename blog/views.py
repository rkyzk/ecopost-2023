from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from .models import Post, Comment, CATEGORY
from datetime import datetime, timedelta
from .filters import PostFilter
import django_filters
from .forms import CommentForm, PostForm

# Set the minimum number of likes so posts with a greater number of likes
# will be included in "Popular Stories"
min_num_likes = 1


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


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, View):

    def post(self, request, id, *args, **kwargs):
        """
        Changes the status of comments to 2 ('Deleted').
        arguments: id: comment id
        :returns: HttpResponseRedirect()
        :rtype: method
        """
        comment = get_object_or_404(Comment, id=id)
        # comment_status 2 indicates 'Deleted'
        comment.comment_status = 2
        comment.save()
        slug = comment.post.slug
        message = 'Your comment has been deleted.'
        messages.add_message(request, messages.SUCCESS, message)
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


class PopularStories(generic.ListView):
    """
    Get posts liked more than once from DB,
    send the queryset and display 'Popular Stories' page.
    """
    model = Post
    template_name = "popular_stories.html"
    paginate_by = 6
    queryset = Post.objects.filter(
            status=2,
            featured_flag=False,
            num_of_likes__gte=min_num_likes
        ).order_by("-published_on")


class Search(View):
    """Hold functions to search posts by multiple factors."""

    def get(self, request, *args, **kwargs):
        """
        Display "Search Stories" page, receive users' input,
        run search based on the input, return a queryset of
        the matching posts and display the search results.
        arguments: self, request, *args, **kwargs
        :returns: render()
        :rtype: method
        """
        # get category choices for the select box
        category_choices = Post._meta.get_field('category').choices
        categories = [cat[1] for cat in category_choices]
        # get country choices for the select box
        country_choices = Post._meta.get_field('country').choices
        countries = [country.name for country in country_choices]
        # Get posts that have been published, arranged from the
        # newest to oldest published dates
        posts = Post.objects.filter(status=2).order_by('-published_on')
        # no_input will be set to false if there's any input
        no_input = True
        queryset = []
        search_clicked = False
        # set search_clicked to True if the 'search' was clicked.
        if 'search' in self.request.GET:
            search_clicked = True
            # get input data in the search form
            title = request.GET.get('title_input')
            author = request.GET.get('author_input')
            kw_1 = request.GET.get('keyword_1')
            kw_2 = request.GET.get('keyword_2')
            kw_3 = request.GET.get('keyword_3')
            min_liked = request.GET.get('liked_count_min')
            pub_date_min = request.GET.get('date_min')
            pub_date_max = request.GET.get('date_max')
            category = request.GET.get('category')
            city = request.GET.get('city')
            country = request.GET.get('country')
            # set initial values for the following variable
            # so filtering doesn't cause any errors.
            if min_liked == "":
                min_liked = "0"

            if title.strip() != "" or author.strip() != "" or kw_1.strip() != "" or kw_2.strip() != "" or kw_3.strip() != "" or country != "Choose..." or city.strip() != "" or min_liked != "0" or category != "Choose...":
                no_input = False

            multiple_q = Q(Q(title__icontains=title.strip()) &
                           Q(author__username__icontains=author.strip()) &
                           Q(num_of_likes__gte=min_liked) &      
                           Q(city__icontains=city) &
                           (Q(title__icontains=kw_1.strip()) |
                            Q(content__icontains=kw_1.strip())) &
                           (Q(title__icontains=kw_2.strip()) |
                            Q(content__icontains=kw_2.strip())) &
                           (Q(title__icontains=kw_3.strip()) |
                            Q(content__icontains=kw_3.strip())))

            # As for the following fields, add to multiple_q only if there's
            # input (otherwise filtering will result in errors.)
            if pub_date_max is not None and pub_date_max != '':
                no_input = False
                max_date = datetime.strptime(
                    pub_date_max, '%Y-%m-%d').strftime('%Y-%m-%d')
                multiple_q &= Q(published_on__lte=max_date)
            if pub_date_min is not None and pub_date_min != '':
                no_input = False
                min_date = datetime.strptime(
                    pub_date_min, '%Y-%m-%d').strftime('%Y-%m-%d')
                multiple_q &= Q(published_on__gte=min_date)
            if country != "Choose...":
                multiple_q &= Q(country__name=country)
            if category != 'Choose...':
                # get category's key from the value
                category_dict = dict(CATEGORY)
                keys = list(category_dict.keys())
                values = list(category_dict.values())
                category_key = keys[values.index(category)]
                multiple_q &= Q(category=category_key)
            if not no_input:
                queryset = posts.filter(multiple_q)

        context = {
            'categories': categories,
            'countries': countries,
            'queryset': queryset,
            'search_clicked': search_clicked,
            'no_input': no_input
        }
        return render(request, "search.html", context)


class Search2(View):
    """Hold functions to search posts by multiple factors."""

    def get(self, request, *args, **kwargs):
        """
        Display "Search Stories" page, receive users' input,
        run search based on the input, return a queryset of
        the matching posts and display the search results.
        arguments: self, request, *args, **kwargs
        :returns: render()
        :rtype: method
        """
        # get category choices for the select box
        category_choices = Post._meta.get_field('category').choices
        categories = [cat[1] for cat in category_choices]
        # get country choices for the select box
        country_choices = Post._meta.get_field('country').choices
        countries = [country.name for country in country_choices]
        # Get posts that have been published, arranged from the
        # newest to oldest published dates
        posts = Post.objects.filter(status=2).order_by('-published_on')
        postFilter = PostFilter(request.GET, queryset=posts)
        posts = postFilter.queryset

        context = {
            'categories': categories,
            'countries': countries,
            'posts': posts,
            'postFilter': postFilter,
        }
        return render(request, "search2.html", context)
