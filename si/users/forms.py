from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class User_registration_form(UserCreationForm):
    username = forms.CharField(label = "Nombre")
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmacion de Contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {k: "" for k in fields}