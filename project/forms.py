from django import forms
from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from project.models import Profile, Post, Community, Comment

# class SignUpForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'password', 'email']


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    display_name = forms.CharField(max_length=30)
    password = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField(label="Enter a Valid Username")
    password = forms.CharField(label="Enter a Valid Password", widget=forms.PasswordInput())
    
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

class EditCommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ['comm_name', 'comm_about', 'comm_url']