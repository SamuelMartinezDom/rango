from distutils.command.upload import upload
from email.mime import image
from re import T
from django.db import models
from django.forms import CharField

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=600, null=True, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)

def __str__(self):
    return self.name 