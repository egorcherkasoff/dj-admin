from django.db import models
from ..products.models import Product
from django.utils import timezone


# Create your models here.
class Shipment(models.Model):
    series = models.CharField(max_length=100, null=False, blank=False, db_index=True)
    comment = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted = timezone.now()
        self.save()

    def __str__(self):
        return self.series


class ShipmentProducts(models.Model):
    shipment = models.ForeignKey(to=Shipment, on_delete=models.CASCADE)
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="shipment_products"
    )
    amount = models.IntegerField(blank=False)
