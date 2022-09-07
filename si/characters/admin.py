from django.contrib import admin
from characters.models import Character


admin.site.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name','description','clase','alineamiento','age', "lvl"]