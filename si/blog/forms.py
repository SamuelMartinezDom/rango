from django import forms

class fomrularios_blog(forms.Form):
    title = forms.CharField(max_length=40)
    body = forms.CharField(max_length=1200)
    date = forms.DateField()#, blank= True)
    author = forms.CharField(max_length=40)
    image = forms.ImageField(required=False)