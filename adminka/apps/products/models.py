from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=512, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=9, null=False, blank=False)
    amount = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"


class ProductImage(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="images",
        related_query_name="product",
    )
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return f"{self.product.name}'s image"

    class Meta:
        verbose_name = "product_image"
        verbose_name_plural = "product_images"
