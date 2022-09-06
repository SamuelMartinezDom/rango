from django.contrib import admin
from users.models import UserProfile


@admin.register(UserProfile)
class user_profile_admin(admin.ModelAdmin):
    list_display = ["user", "favorite_class", "image"]