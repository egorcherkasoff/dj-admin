from django.db import models
from django.utils import timezone


# Create your models here.
class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ("success", "Positive"),
        ("warning", "Warning"),
        ("danger", "Error"),
        ("info", "Info"),
    ]

    text = models.CharField(max_length=155, null=False, blank=False)
    allow_dates = models.BooleanField(
        null=True, default=True, blank=True
    )  # display dates on home page or not
    type = models.CharField(
        null=False, blank=False, choices=NOTIFICATION_TYPES, max_length=15
    )
    start = models.DateTimeField(null=False, blank=False)
    end = models.DateTimeField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.text[:15]}.. {self.start.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "notification"
        verbose_name_plural = "notifications"
