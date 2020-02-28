from django.db import models
from django.contrib.auth.models import User
from django import forms
import random


# création d'une classe mesusers pour tout mon site qui a comme plus un numéro de téléphone
# et une image
class MesUsers(User):
    numerotel = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        )


# un client peut avoir son responsableuet de meme profil il est client aussi (elle hérite de
# mes users)
class Client(MesUsers):
    responsableUET=models.ForeignKey('self', blank = True, null=True)
    
    class Meta:
        verbose_name='Client'


# generer mot de passe automatique aleatoire
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


class Role(models.Model):

    role_name = models.CharField(
        max_length= 150,
        unique=True
    )

    def __str__(self):
        return self.role_name


class UserSite(MesUsers):
    role = models.ForeignKey(Role, null=True,on_delete=models.CASCADE)

    poste = models.ForeignKey(
        NewPostName,  
        null=True, 
        blank=True, 
        on_delete=models.PROTECT, 
        )
    
    class Meta:
        verbose_name='User du site'


# un user chef hérite de mes user et il peut avoir un responsable qui a un profil chef comme
# lui
class Chef(UserSite):
    responsable=models.ForeignKey('self', blank = True, null=True)

    class Meta:
        verbose_name='Responsable d\'activitées / SOP'


# un user chef de projet hérite de mes user et il peut avoir un responsable chef
class ChefdeProjet(UserSite):
    responsable=models.ForeignKey(Chef)
    
    class Meta:
        verbose_name='chef de projet'


# rt son responsbale c'est un chef
class Rt(UserSite):
    responsable=models.ForeignKey(ChefdeProjet)
    
    class Meta:
        verbose_name='Rt'


class Liv(UserSite):
    responsable=models.ForeignKey(Rt)
    executant = models.ManyToManyField('ChValid', blank=True, related_name='liv')

    class Meta:
        verbose_name='Pilote d\'activité'


class ChValid(UserSite):
    responsable=models.ForeignKey(Liv)

    class Meta:
        verbose_name='Executant'

    def __str__(self):
        return str(self.user.username) 







        







    


