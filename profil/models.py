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
        ('pilote_activite', 'PILOTE D\'ACTIVITÉ'),
        ('charge_execution', 'CH.EXECUTION'),
        
    ) 
    IS_ACTIVE = (
        ('activate', 'actif'),
        ('desactivate', 'desactive '),
        
    )
    POSTE = (
        
        ('ch.MIL', 'CH.MIL'),
        ('ch.HIL', 'CH.HIL'), 
        ('ch.IS', 'CH.IS'),
        ('liv', 'LIV'),
        ('rt', 'RT'),
        ('pmo', 'PMO'),
        ('rsop', 'RSOP'),
        
    ) 

    poste = models.CharField(max_length=150, choices=POSTE )

    poste.widget = forms.TextInput(attrs={'class': 'form-control',})
    
    image = models.ImageField(
            upload_to=upload_location,
            null=True,
            blank=True,
            
        )
   
    role = models.CharField( max_length=20 ,choices=ROLES, default='charge_execution')

    is_active = models.CharField(null=True, blank=True, max_length=15 ,choices=IS_ACTIVE, default='activate')


  

    def __str__(self):
        return self.user.username



    

class Liv(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    

    #equipe = models.ForeignKey("Chvalid", on_delete=models.SET_NULL)
   
    executant = models.ManyToManyField('ChValid', blank=True)
    
    
    
    

    def __str__(self):
        return self.user.username
    



class ChValid(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   

   # superieur = models.ManyToManyField(Liv)

    responsable = models.ForeignKey(Liv, null=True, blank=True,  on_delete=models.CASCADE)

    

   

    def __str__(self):
        return self.user.username