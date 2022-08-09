from django import forms

class fomrularios_character(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=100)
    age = forms.IntegerField()
    clase = forms.CharField(max_length=13)
    lvl = forms.IntegerField()