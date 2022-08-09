from re import T
from django.db import models
from django.forms import CharField

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, null=True, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()

def __str__(self):
    return self.name 