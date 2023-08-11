"""This module holds forms used in ecopost."""

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Form for comments."""
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': ''}
