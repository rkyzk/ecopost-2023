"""This module holds forms used in ecopost."""

from .models import Comment, Post, CATEGORY
from django import forms


class PostForm(forms.ModelForm):
    """Form for posts."""

    class Meta:
        """Features of PostForm."""
        model = Post
        fields = ['title', 'content', 'featured_image',
                  'city', 'category']
        title = forms.CharField(required=True)
        content = forms.CharField(required=True)
        city = forms.CharField(required=True)

        def __init__(self, *args, **kwargs):
            """Set required flag of featured image to False."""
            self.fields['featured_image'].required = False
            super(PostForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    """Form for comments."""
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'comment'}
