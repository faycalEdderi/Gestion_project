from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


# fonction qui prends tout les objets d'une classe et les renvoi dans une liste
def choix(objectmodel):
    liste = objectmodel.objects.all()  
    l = []
    for q in liste:
        l.append((q.nom , q.nom))
    return l


# création de type d'uo pour chaque uo un type
class Typeuo(models.Model):
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom  


# création de niveau d'uo pour chaque uo un niveau
class Niveauuo(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom 


# création de catalogue uo et que pour chaque type et niveau un prix et un nombre de jour
class CatalogueUo(models.Model):
    nom=models.CharField(max_length=20)
    typeuo=models.ForeignKey(Typeuo, on_delete=models.CASCADE,default = "")
    niveauuo=models.ForeignKey(Niveauuo, on_delete=models.CASCADE,default = "")
    nbrjouruo=models.CharField(max_length=5)
    prixuo=models.CharField(max_length=20)

    def __str__(self):
        return self.nom   


# création de périmetre et pour chaque périmetre un catalogue uo à respecter
class Perimetre(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
        return self.nom 

      
# création de work package et pour chaque wp plusieurs périmetres
class WorkPackage(models.Model):
    nom=models.CharField(max_length=20)
    perimetretravail=models.ForeignKey(Perimetre, 
    on_delete=models.CASCADE,
    default = "")

    def __str__(self):
        return self.nom 


# création de table fonction
class Fonction(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom  


# création de statut uo comme une table pour qu'il puisse rajouter des statut ou modifier ou
# suprrimer
class Statutuo(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom


# création d'état uo comme une table pour qu'il puisse rajouter des états ou modifier ou
# suprrimer
class Etatuo(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom


# création de projet comme une table pour qu'il puisse rajouter des projet ou modifier ou
# suprrimer
class Projet(models.Model):
    nom=models.CharField(max_length=20)

    def __str__(self):
       return self.nom


# création de platforme et pour chaque platforme des projets differents
class Plateforme(models.Model):
    nom=models.CharField(max_length=20)
    projets = models.ForeignKey( Projet, on_delete=models.CASCADE,default = "")

    def __str__(self):
       return self.nom


# création d'uet et pour chaque uet des fonctions differentes
class Uet(models.Model):
    nom=models.CharField(max_length=20)
    fonctions = models.ForeignKey(Fonction, on_delete=models.CASCADE,default = "")

    def __str__(self):
       return self.nom


class Lot(models.Model):
    nom=models.CharField(max_length=50)

    def __str__(self):
       return self.nom


# création d'uo avec possiblité de choisir les champs dans des table differente
class Uo(models.Model):
    numuo = models.CharField(max_length=20)
    typeuo = models.ForeignKey(Typeuo,default = "",on_delete=models.CASCADE)
    niveauo = models.ForeignKey(Niveauuo,default = "",on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet,default = "",on_delete=models.CASCADE)
    fonction = models.ForeignKey(Fonction,default = "",on_delete=models.CASCADE)
    statutuo = models.ForeignKey(Statutuo,default = "",on_delete=models.CASCADE)
    etatuo = models.ForeignKey(Etatuo,default = "",on_delete=models.CASCADE)
    plateforme = models.ForeignKey(Plateforme,default = "",on_delete=models.CASCADE)
    uet = models.ForeignKey(Uet,default = "",on_delete=models.CASCADE)
    catalogue = models.ForeignKey(CatalogueUo,default = "",on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot,default = "",on_delete=models.CASCADE)
    jalonD = models.CharField(max_length=20,default="")
    jalonF = models.CharField(max_length=20,default="")
    ju = models.CharField(max_length=20,default="")
    DateDebutUO=models.DateTimeField(default=timezone.now(),blank=True)
    DateLivraison=models.DateTimeField(default=timezone.now(),blank=True)
    Client=models.CharField(max_length=20,default="")
    avancement=models.FloatField(default=0)
    piloteUo=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.numuo  #+ "  " + self.typeuo + "   " + self.niveauo + "   " + self.projet + "   " + self.fonction + "   " + self.platforme + "   " + self.uet 


# class pointage qui permet aux utilisateur de pointer sur l'uo
class Pointage(models.Model):
    uo =models.ForeignKey(Uo,on_delete=models.CASCADE,default = "")
    user=models.ForeignKey(User,on_delete=models.CASCADE,default = "")
    semaine= models.IntegerField()
    point=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5)])

    def __str__(self):
       return str(self.point)


# class note de cadrage pour chaque uo une note de cadrage 'reflichir pour apres si on peut ajouter des numero pour les modification de note de cadrage  '
class NotedeCadrage(models.Model):
    uo=models.ForeignKey(Uo,on_delete=models.CASCADE,default = "")
    reponseRSA=models.CharField(max_length=600,default="")

  
# classe activités pour chaque note de cadrage plusieur activitées 
class Activites(models.Model):
    notedeCadrage=models.ForeignKey(NotedeCadrage,on_delete=models.CASCADE,default = "")
    donnesdentree=models.CharField(max_length=600,default="")
    activiteAttendue=models.CharField(max_length=600,default="")	
    pourcentagedactivite=models.FloatField()
    Conditionsdereussite=models.CharField(max_length=600,default="")	
    Datedonnéesdentrees=models.DateTimeField(default="", blank=True)
    DatedeDemarragedActivite=models.DateTimeField( default="",blank=True)
    LivrableAttendu=models.CharField(max_length=600,default="")	
    DatedeReceptionAttenduduLivrable=models.DateTimeField(default="", blank=True)
    CommentairesSurAttendu=models.CharField(max_length=600,default="")	



