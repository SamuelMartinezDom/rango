from django.db import models

#··$%$·"!%& Create your models here.

class article(models.Model):
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=1200)
    date = models.DateField(auto_now_add=True, null=True)#, blank= True)
    author = models.CharField(max_length=40)

def __str__(self):
    return self.title 