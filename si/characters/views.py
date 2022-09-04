from django.shortcuts import render, redirect
from characters.models import character
from characters.forms import fomrularios_character
from django.contrib.auth.decorators import login_required

@login_required
def create_character(request):
    if request.method == 'POST': 
     form= fomrularios_character(request.POST)

     if form.is_valid():
            character.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                age = form.cleaned_data['age'],
                clase = form.cleaned_data['clase'],
                lvl = form.cleaned_data['lvl']
            )     
            return redirect(characters)
     
    elif request.method == 'GET':
     form_character = fomrularios_character
     context = {'form_character':form_character}
    return render(request, "characters/new_character.html", context=context)

@login_required
def characters(request):
    characters= character.objects.all()
    context = {"characters": characters}
    return render(request, "characters/characters.html", context=context)