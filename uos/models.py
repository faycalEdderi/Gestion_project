from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#fonction qui prends tout les objets d'une classe et les renvoi dans une liste 
def choix(objectmodel):
    liste = objectmodel.objects.all()  
    l = []
    for q in liste:
        l.append((q.nom , q.nom))
    return l

class typeuo(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
        return self.nom  

class niveauuo(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom  
       
class fonction(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom  



class statutuo(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom

class etatuo(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom

class projet(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom

class plateforme(models.Model):
    nom=models.CharField(max_length=20)
    Projets = models.ForeignKey( projet, on_delete=models.CASCADE,default = "")

    def __str__(self):
       return self.nom

class UET(models.Model):
    nom=models.CharField(max_length=20)
    fonctions = models.ForeignKey(fonction, on_delete=models.CASCADE,default = "")

    def __str__(self):
       return self.nom
       

class uo(models.Model):
    numuo = models.CharField(max_length=20)
    typeuo = models.CharField(default = 0,max_length=20, choices = choix(typeuo))
    niveauo = models.CharField(default = 0,max_length=20, choices = choix(niveauuo))
    projet = models.CharField(default = 0,max_length=20, choices = choix(projet))
    fonction = models.CharField(default = 0,max_length=20, choices = choix(fonction))
    statutuo=models.CharField(default = 0,max_length=20, choices = choix(statutuo))
    etatuo=models.CharField(default = 0,max_length=20, choices = choix(etatuo))
    plateforme=models.CharField(default = 0,max_length=20, choices = choix(plateforme))
    UET=models.CharField(default = 0,max_length=20, choices = choix(UET))

    def __str__(self):
        return self.numuo  +"  "+ self.typeuo +"   " +self.niveauo