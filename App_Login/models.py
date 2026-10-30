from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE
    )
    profile_pic = models.ImageField(upload_to='profile_pics',null=True, blank=True)
    date_of_birth = models.DateField()
    website = models.URLField(null=True, blank=True)
    facebook_account = models.URLField(null=True, blank=True)