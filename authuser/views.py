from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout

from authuser.forms import LoginForm, SignUpForm
from authuser.models import Profile


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
            return HttpResponseRedirect(reverse('homepage'))
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