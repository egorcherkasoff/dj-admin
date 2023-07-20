from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
import uuid
from django.utils import timezone


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    email = models.EmailField(unique=True, null=False, blank=False)
    avatar = models.ImageField(null=True, blank=True, upload_to="")

    first_name = models.CharField(max_length=60, null=True, blank=True)
    middle_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)

    last_activity = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name

    def delete(self):
        self.deleted = timezone.now()
        self.is_active = False
        self.save()
