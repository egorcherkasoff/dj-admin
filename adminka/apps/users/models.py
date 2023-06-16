from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    username = models.CharField(null=True, blank=True, max_length=25, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    avatar = models.ImageField(null=True, blank=True, upload_to="")
    middle_name = models.CharField(max_length=60, null=True, blank=True)
    last_activity = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return self.username
