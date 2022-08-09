from django.shortcuts import render
from characters.models import character
from characters.forms import fomrularios_character
# Create your views here.

def create_character(request):
    if request.method == 'POST':
     print(request.Post)
     new_character = character.objects.create(
        name = "Magnus El Maldito",
        description = "si",
        age = 35,
        clase = "Barbaro",
        lvl = 10)
     context = {
        "new_character": new_character
     }
    elif request.method == 'GET':
     form_character = fomrularios_character
     context = {'form_character':form_character}
    return render(request, "characters/new_character.html", context=context)

def characters(request):
    characters= character.objects.all()
    context = {"characters": characters}
    return render(request, "characters/characters.html", context=context)