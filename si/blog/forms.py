import datetime
from django import forms


class FormularioBlog(forms.Form):

    
    """Modelo de formulario para la creacion de articulos."""
    title = forms.CharField(max_length=40)
    body = forms.CharField(max_length=1200)
    date = forms.DateField(initial=datetime.date.today())
    author = forms.CharField(max_length=40)
    image = forms.ImageField(required=False)