from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(null=True, blank=False)
    middle_name = models.CharField(max_length=60, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username
