from django import forms

class fomrularios_productos(forms.Form):
    name = forms.CharField(max_length=30)
    category = forms.CharField(max_length=30)
    price = forms.FloatField()
    stock = forms.IntegerField()