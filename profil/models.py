from django import forms
from django.db import models
from django.contrib.auth.models import User
import random


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    filebase= ''.join((random.choice(chars)) for x in range(20))
    
    return "%s/%s.%s" %(instance.id, filebase, extension)


class NewPostName(models.Model):
    
    post_name = models.CharField(
        max_length=150,
        unique=True, 
        error_messages={'unique':"Ce poste existe déja !"},
        )

    def __str__(self):
        return self.post_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLES = (
        ('pmo', 'PMO'),
        ('rsop', 'RSOP'),
        ('rt', 'RT'),
        ('pilote_activite', 'PILOTE D\'ACTIVITÉ'),
        ('charge_execution', 'CH.EXECUTION'),
    )

    IS_ACTIVE = (
        ('activate', 'actif'),
        ('desactivate', 'desactive '),
    )
 
    poste = models.ForeignKey(
        NewPostName,  
        null=True, 
        blank=True, 
        on_delete=models.PROTECT, 
        )

    image = models.ImageField(
            upload_to=upload_location,
            null=True,
            blank=True,
        )
   
    role = models.CharField(

        max_length=20 ,
        choices=ROLES,
        default='charge_execution'
    )



    def __str__(self):
        return self.user.username


class Rt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Liv(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    executant = models.ManyToManyField('ChValid', blank=True, related_name='liv')
    rt_liv = models.ForeignKey(Rt, null=True, blank=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ChValid(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Liv, null=True, blank=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username







