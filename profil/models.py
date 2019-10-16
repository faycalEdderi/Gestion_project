from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    poste = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.user.username
    

