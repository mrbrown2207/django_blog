from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Only fields that are editable
        fields = ('title', 'content', 'image', 'tag', 'published_date')