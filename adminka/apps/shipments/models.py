from django.db import models
from ..products.models import Product
from django.utils import timezone


# Create your models here.
class Shipment(models.Model):
    series = models.CharField(max_length=100, null=False, blank=False, db_index=True)
    product = models.ManyToManyField(
        to=Product, related_name="products", related_query_name="shipments"
    )
    amount = models.IntegerField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted = timezone.now()
        self.save()

    def __str__(self):
        return self.series
