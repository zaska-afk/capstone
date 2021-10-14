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
from authuser.views import login_view, logout_view, signup_view, profile_view, edit_profile_view
# handler404 = 'project.views.handler404'
# handler500 = 'project.views.handler500'

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
    path('user/<int:id>/', views.UserView, name='user'),
    path( '',views.handler404 ),
    path( '',views.handler500 ),
    path('editprofile/<int:user_id>/', edit_profile_view),
    path('profile/<int:user_id>/', profile_view),
    path("community_id/<int:id>/", views.community_view, name="community_id"),
    path("editCommunity/<int:id>/", views.editCommunity, name='editcommunity')
    
    # path("posts/<int:id>/", views.post_detail, name="post"),
    # path("community/<int:id>/", views.community_detail, name="community"),
]
