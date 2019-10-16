from django.db import models
from django.contrib.auth.models import User

import random



def upload_location(instance, filename):
    filebase, extension = filename.split(".")

    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    filebase= ''.join((random.choice(chars)) for x in range(20))
    
    return "%s/%s.%s" %(instance.id, filebase, extension)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    poste = models.CharField(max_length=150)
    image = models.ImageField(
            upload_to=upload_location,
            null=True,
            blank=True, 
        )


    def __str__(self):
        return self.user.username
    

