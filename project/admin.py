from django.contrib import admin
from project.models import Post, Profile, Comment, Community
# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Community)