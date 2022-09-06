from django import forms


class FormulariosBlog(forms.Form):

    
    """Modelo de formulario para la creacion de articulos."""
    title = forms.CharField(max_length=40)
    body = forms.CharField(max_length=1200)
    date = forms.DateField()
    author = forms.CharField(max_length=40)
    image = forms.ImageField(required=False)