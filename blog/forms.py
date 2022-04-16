from django.forms import ModelForm
from .models import Comment, Post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name' , 'body']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author_id', 'title', 'header_image', 'content']