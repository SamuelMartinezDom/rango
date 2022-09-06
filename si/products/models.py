from re import T
from django.db import models

# Create your models here.

class Product(models.Model):
    """Modelo de productos en general"""
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=600, null=True, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)

def __str__(self):
    return self.name 