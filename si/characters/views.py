from django.shortcuts import render
from characters.models import character
# Create your views here.

def create_character(request):
    new_character = character.objects.create(
        name = "Magnus El Maldito",
        description = "si",
        age = 35,
        clase = "Barbaro",
        lvl = 10)
    context = {
        "new_character": new_character
    }
    return render(request, "characters/new_character.html", context=context)

def characters(request):
    characters= character.objects.all()
    context = {"characters": characters}
    return render(request, "characters/characters.html", context=context)