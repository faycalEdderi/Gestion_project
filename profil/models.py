from django import forms
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

    ROLES = (
        #AJOUTER Ch valid
        ('rt', 'RT'),
        ('liv', 'LIV ')
    ) 
    IS_ACTIVE = (
        ('activate', 'actif'),
        ('desactivate', 'desactive ')
    ) 

    poste = models.CharField(max_length=150)
    image = models.ImageField(
            upload_to=upload_location,
            null=True,
            blank=True,
            
        )
   
    role = models.CharField( max_length=9 ,choices=ROLES, default='liv')

    is_active = models.CharField(null=True, blank=True, max_length=15 ,choices=IS_ACTIVE, default='activate')

  

    def __str__(self):
        return self.user.username
    

