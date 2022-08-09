from django.db import models

# Create your models here.

class character(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    age = models.IntegerField()
    clase = models.CharField(max_length=13)
    lvl = models.IntegerField()

def __str__(self):
    return self.title 