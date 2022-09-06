from django.urls import path, include
from characters.views import create_character, characters, update_character, delete_character

urlpatterns = [
    path("characters/", characters, name= "characters"),
    path('create_character/', create_character, name= 'create_character'),
    path('delete_character/<int:pk>/', delete_character, name='delete_character'),
    path('update_character/<int:pk>/', update_character, name='update_character')
]