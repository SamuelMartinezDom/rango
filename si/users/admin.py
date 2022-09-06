from django.contrib import admin
from users.models import user_profile

# Register your models here.

@admin.register(user_profile)
class user_profile_admin(admin.ModelAdmin):
    list_display = ["user", "favorite_class", "image"]