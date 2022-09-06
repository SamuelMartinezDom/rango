from django import forms

class FomrulariosCharacter(forms.Form):
    """Modelo de formulario para la creacion de personajes"""
    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=100)
    age = forms.IntegerField()
    clase = forms.CharField(max_length=13)
    lvl = forms.IntegerField()
    image = forms.ImageField(required=False)