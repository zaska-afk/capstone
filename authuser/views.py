from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
# from authuser import serializers
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.generics import GenericAPIView
# from .serializers import GoogleSocialAuthSerializer

from authuser.forms import LoginForm, SignUpForm, EditProfileForm
from authuser.models import Profile
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# from authuser.serializers import GoogleSocialAuthSerializer


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            profile = Profile.objects.create(
                display_name=data["display_name"],
                user=user
                )
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = SignUpForm
    return render(request, 'signup.html', {'form': form})
    
    
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def profile_view(request, user_id):
    user = Profile.objects.get(id=user_id-1)
    return render(request, "profile.html", {"user": user})


# @login_required
def edit_profile_view(request, user_id):
    print(type(user_id))
    item = Profile.objects.get(id=user_id)

    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            item.bio = data['bio']
            item.display_name = data['display_name']
            item.save()
            return HttpResponseRedirect(
                reverse('homepage')
            )

    form = EditProfileForm(initial={
        "bio": item.bio,
        'display_name': item.display_name
    })

    return render(request, 'generic_form.html', {"form": form})


# class GoogleSocialAuthView(GenericAPIView):
#     serializer_class = GoogleSocialAuthSerializer

#     def post(self, request):
#         '''POST with "auth_token"
#         send an idtoken as from google to get user information'''

#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = ((serializer.validated_data)['auth_token'])
#         return Response(data, status=status.HTTP_200_ok)
