from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth.models import Profile


admin.site.register(Profile, UserAdmin)
