from django import forms


class FormularioCharacters(forms.Form):


    """Modelo de formulario para la creacion de personajes"""
    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=100)
    alineamiento = forms.CharField(max_length=20, required=False)
    age = forms.IntegerField()
    clase = forms.CharField(max_length=20)
    lvl = forms.IntegerField()
    image = forms.ImageField(required=False)