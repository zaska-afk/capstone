"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views
from project.views import index, addcomment_view, addcommunity_view, addpost_view
from authuser.views import login_view, logout_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="homepage"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("addcommunity/", addcommunity_view, name="addcommunity"),
    path("addcomment/", addcomment_view, name="addcomment"),
    path("addpost/", addpost_view, name="addpost"),
    path('upvote/<int:post_id>/', views.upvote_view , name="like"),
    path('downvote/<int:post_id>/', views.downvote_view, name="dislike"),
    
    # path("posts/<int:id>/", views.post_detail, name="post"),
    # path("community/<int:id>/", views.community_detail, name="community"),
]
