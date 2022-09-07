from django.urls import path
from characters.views import create_character, characters, delete_character, update_character


urlpatterns = [
    path("characters/", characters, name= "characters"),
    path('create_character/', create_character, name= 'create_character'),    
    path('delete_character/<int:id>/', delete_character, name='delete_character'),
    path('update_character/<int:id>/', update_character, name='update_character')]