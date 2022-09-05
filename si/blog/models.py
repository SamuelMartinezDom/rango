from django.db import models

#··$%$·"!%& Create your models here.

class Article(models.Model):
    """Modelo para los articulos, como guias, etc."""
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=3200)
    date = models.DateField(auto_now_add=True, null=True)#, blank= True)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='article/', null=True, blank=True)

def __str__(self):
    return self.title 