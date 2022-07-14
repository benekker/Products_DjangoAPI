
from django.db import models

from products.models import Product


# Create your models here.

class Review(models.Model):
    rating = models.DecimalField(max_digits=1, decimal_places=1)
    description = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)