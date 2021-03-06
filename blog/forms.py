from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text', 'title', 'url', 'source', 'image', 'top_sent', 'trogram',)
