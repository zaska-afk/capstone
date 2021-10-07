from django import forms
from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from project.models import Post, Community, Comment


# Dunya - commented out 'post_on_comm' to render post form
class AddPostForm(ModelForm):
    class Meta:
        model = Post
        # fields = ['post_name', 'post_text', 'post_on_comm']
        fields = ['post_name', 'post_text',"post_on_comm"]


class AddCommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ['comm_name', 'comm_about', 'comm_url']


class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['on_post','comment_text']


class EditCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['on_post', 'comment_text']
