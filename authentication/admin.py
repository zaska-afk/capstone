from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import Profile


admin.site.register(Profile, UserAdmin)
