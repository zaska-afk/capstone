from django.shortcuts import render,HttpResponse, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.template import RequestContext
from django.http import Http404
from django.views import View 
from project.forms import AddCommunityForm, AddPostForm, EditCommentForm, LoginForm, SignUpForm, AddCommentForm, EditCommunityForm
from project.models import Comment, Profile, Community, Post
import re
# Create your views here.

def navbar_view(request):
    return render(request, 'navbar.html')

@login_required
def index(request):
    template_name = 'index.html'
    posts = Post.objects.all()
    return render(request, template_name, {"posts": posts})


def edit(request, id):
    if not request.user.is_staff or request.user.author == Post.post_creator:
        return HttpResponse("Access Denied - Need staff/admin permissions")
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=post)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = EditCommentForm(initial=model_to_dict(post))
    return render(request, "generic_form.html", {'form': form})


def addpost_view(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            # form.save()
            data = form.cleaned_data
            author = Post.objects.create(
                post_name = data.get("post_name"),
                post_text = data.get("post_text"),
                post_on_comm = data.get("post_on_comm"),
            )
            return redirect('/')
    else:
        form = AddPostForm()
    return render(request, "post.html", {"form": form})


def addcomment_view(request):
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment.objects.create(
            on_post = data.get("on_post"),
            comment_text = data.get("comment_text"),
            )
        return redirect('/')
    else:
        form = AddCommentForm()
    return render(request, "comment.html", {"form": form})


def addcommunity_view(request):
    if request.method == "POST":
        form = AddCommunityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            community = Community.objects.create(
            comm_name = data.get("comm_name"),
            comm_about = data.get("comm_about"),
            comm_creator = data.get("comm_creator"),
            )
        return redirect('/')
    else:
        form = AddCommunityForm()
    return render(request, "community.html", {"form": form})


class UpVoteView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.credit += 1
        post.save()
        return HttpResponseRedirect('/')



class DownVoteView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.credit -= 1
        post.save()
        return HttpResponseRedirect('/')        



def commentlist_view(request, id: str):
    post = Post.objects.get(id=id)
    community = Post.post_on_comm
    comments = Comment.objects.filter(id = id)
    comments = post.comments.all()
    return render(request, 'comment_list.html', {'comments': comments})

class CommunityView(View):
    def get(self, request, id: str):
        com = Community.objects.get(id=id)
        return render(request, "community_id.html", {"com": com})


def editCommunity(request, id):
    if request.user.is_staff == Community.comm_creator:
        return HttpResponse("Access Denied - Need staff/admin permissions")
    com = Community.objects.get(id=id)

    if request.method == 'POST':
        form = EditCommunityForm(request.POST, instance=com)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = EditCommunityForm(initial=model_to_dict(com))
    return render(request, "generic_form.html", {'form': form})


def handler404(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, '404.html', {'poll': post})

def handler500(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, '500.html', {'poll': post})