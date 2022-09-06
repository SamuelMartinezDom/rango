from django.db import models

# Create your models here.

class Character(models.Model):
    """Modelo basico de personajes para rol"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    age = models.IntegerField()
    alineamiento = models.CharField(max_length=50, null=True, blank=True)
    clase = models.CharField(max_length=50)
    lvl = models.IntegerField()
    image = models.ImageField(upload_to='character/', null=True, blank=True)

def __str__(self):
    return self.name