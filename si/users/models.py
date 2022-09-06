from distutils.command.upload import upload
from django.db import models


class UserProfile(models.Model):

    
    user = models.OneToOneField("auth.User", on_delete= models.CASCADE, related_name="profile")
    favorite_class = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to="profile_images/", blank=True)

    def __str__(self):
        return self.user.username + " - profile"