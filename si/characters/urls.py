from django.urls import path, include
from characters.views import create_character, characters

urlpatterns = [
    path("characters/", characters, name= "characters"),
    path('create_character/', create_character, name= 'create_character')
]