
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    display_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=200, blank=True)
    credit = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.display_name