from django.shortcuts import render, redirect
from characters.models import Character
from characters.forms import FormularioCharacters
from django.contrib.auth.decorators import login_required


@login_required
def create_character(request):
        if request.method == 'POST': 
            form= FormularioCharacters(request.POST, request.FILES)

            if form.is_valid():
                Character.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],

                age = form.cleaned_data['age'],
                clase = form.cleaned_data['clase'],
                lvl = form.cleaned_data['lvl'])     
                return redirect(characters)
     
            elif request.method == 'GET':
                form_character = FormularioCharacters
                context = {'form_character':form_character}
            return render(request, "characters/create_character.html", context=context)

@login_required
def characters(request):
    characters= Character.objects.all()
    context = {"characters": characters}
    return render(request, "characters/characters.html", context=context)