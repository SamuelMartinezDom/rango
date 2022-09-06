from django.db import models


class Character(models.Model):

    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    alineamiento = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    clase = models.CharField(max_length=50)
    lvl = models.IntegerField()
    image = models.ImageField(upload_to='character/', null=True, blank=True)

def __str__(self):
    return self.name 