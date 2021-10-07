from django.shortcuts import render,HttpResponse, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from project.forms import AddCommunityForm, AddPostForm, EditCommentForm, LoginForm, SignUpForm
from project.models import Comment, Profile, Community, Post, Vote
import re
# Create your views here.
# Dunya added redirect and re to imports
def index(request):
    template_name = 'index.html'
    posts = Post.objects.all()

    return render(request, template_name, {"posts": posts})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            user = Profile.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
            )
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignUpForm
    return render(request, 'generic_form.html', {'form': form})
    
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
    else:
        form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

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
            add_post = Post.objects.create(
                post_content=data["post_name", "post_text", "post_on_comm"],
                # post_content=data["post_name", "post_text"],
                post_creator=request.user
            )
            # if "@" in data["post_text"]:
            #     find_user = re.findall(r"@(\w+)", data["post_content"])
            #     grap_user = find_user[0]
                # user = post_on_comm.objects.get(username=grap_user)
                # Notification.objects.create(post_creator=user, add_post=add_post)
            return redirect('/')

    form = AddPostForm()
    return render(request, "generic_form.html", {"form": form})

# Dunya - took structure some what from recipebox
# Dunya - not sure about the structure
# Dunya - Changed view a bit to help render. commented out olde to have a reference
def addcomment_view(request):
    template_name = "generic_form.html"
    # comment = Post.objects.get(id=id) # Dunya - Not sure about use of id
    comment = Post.objects.create("on_post, comment_text")
    # context = {"comment": comment}
    # return render(request, template_name, context)
    return render(request, template_name)

def addcommunity_view(request):
    ...

def profilepage_view(request):
    ...