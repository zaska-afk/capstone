from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    display_name = models.CharField(max_length=50)
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=200, blank=True)
    credit = models.IntegerField(default=0)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.display_name
