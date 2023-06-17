from django.db import models
from django.contrib.auth.models import User
import os

def get_profile_photo_path(instance, filename):
    username = instance.user
    user_id = instance.user.id

    folder_name = f"{user_id}-{username}"
    return os.path.join('MANIMath_Account', 'static' , 'media', 'profile_photos', folder_name, filename)

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, default=None)
    profile_photo = models.ImageField(default='media/img/Default_Profile_Picture.png', upload_to=get_profile_photo_path, blank=True, null=True)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f'{self.user.username.capitalize()} - Profile'