from re import T
from django.db import models
from django.forms import CharField

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField()
    date_of_birth = models.CharField(max_length=30, null=True)

def __str__(self):
    return self.name 