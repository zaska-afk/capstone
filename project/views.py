from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from project.forms import AddCommunityForm, AddPostForm, EditCommentForm
from project.models import Comment, Profile, Community, Post, Vote
# Create your views here.

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

def home_view(request):
    ...

def addpost_view(request):
    ...

def addcomment_view(request):
    ...

def addcommunity_view(request):
    ...

def profilepage_view(request):
    ...