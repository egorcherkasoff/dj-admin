from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    def delete(self):
        self.deleted = timezone.now()
        self.save()

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
