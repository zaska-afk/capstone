from django.shortcuts import render,HttpResponse, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.template import RequestContext
from django.http import Http404

from project.forms import AddCommunityForm, AddPostForm, EditCommentForm, AddCommentForm, EditCommunityForm
from project.models import Comment, Profile, Community, Post, Vote
import re
# Create your views here.

def index(request):
    template_name = 'index.html'
    posts = Post.objects.all()

    return render(request, template_name, {"posts": posts})

def UserView(request, id):
    html = "user.html"
    user = Profile.objects.get(id=id)
    # ^ Broken here
    posts = Post.objects.filter(author=user).order_by('-date')
    comments = Comment.objects.filter(author=user).order_by('-date')
    communities = Community.objects.filter(author=user).order_by('-date')
    return render(request, html, {'user': user, 'posts': posts})

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

def home_view(request):
    ...
# By Dunya-trying create an add_post with @ user ability
# Dunya - structure somewhat taken from twitterclone(Not sure about lines 84 and 85)
def addpost_view(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            # form.save()
            data = form.cleaned_data
            author = Post.objects.create(
                # post_content=data["post_name", "post_text", "post_on_comm"],
                # post_content=data["post_name", "post_text"],
                post_name = data.get("post_name"),
                post_text = data.get("post_text"),
                post_on_comm = data.get("post_on_comm"),
                # post_creator=request.user
            )
            # if "@" in data["post_text"]:
            #     find_user = re.findall(r"@(\w+)", data["post_content"])
            #     grap_user = find_user[0]
                # user = post_on_comm.objects.get(username=grap_user)
                # Notification.objects.create(post_creator=user, add_post=add_post)
            return redirect('/')
    else:
        form = AddPostForm()
    return render(request, "generic_form.html", {"form": form})


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

def profilepage_view(request):
    ...

def upvote_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.upvote += 1
    post.save()
    return HttpResponseRedirect('/')


def downvote_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downvote += 1
    post.save()
    return HttpResponseRedirect('/')

def community_view(request, id: str):
    com = Community.objects.get(id=id)
    return render(request, "community_id.html", {'com': com})

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