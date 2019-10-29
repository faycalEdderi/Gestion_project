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
        
        ('rt', 'RT'),
        ('liv', 'LIV'),
        ('ch.Valid', 'CH.VALID '),
        
    ) 
    IS_ACTIVE = (
        ('activate', 'actif'),
        ('desactivate', 'desactive '),
        
    )
    POSTE = (
        ('blank', ' '),
        ('ch.MIL', 'CH.MIL'),
        ('ch.HIL', 'CH.HIL '), 
        ('ch.IS', 'CH.IS '),
        ('liv', 'Pilote d\'activité'),
        ('rt', 'RT '),
        ('pom', 'PMO'),
        ('rsop', 'RSOP'),
        
    ) 

    poste = models.CharField(max_length=150, choices=POSTE, default='blank')
    image = models.ImageField(
            upload_to=upload_location,
            null=True,
            blank=True,
            
        )
   
    role = models.CharField( max_length=9 ,choices=ROLES, default='ch.Valid')

    is_active = models.CharField(null=True, blank=True, max_length=15 ,choices=IS_ACTIVE, default='activate')

  

    def __str__(self):
        return self.user.username
    

