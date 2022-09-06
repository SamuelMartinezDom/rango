from django.db import models

class Article(models.Model):
    """Modelo para los articulos, como guias, etc."""
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=3200)
    date = models.DateField(auto_now_add=True, null=True)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='article/', null=True, blank=True)

def __str__(self):
    return self.title 