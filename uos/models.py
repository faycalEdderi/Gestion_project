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

    
# création de work package et pour chaque wp plusieurs périmetres
class WorkPackage(models.Model):
    nom=models.CharField(max_length=20)
    
    def __str__(self):
        return self.nom 


# création de périmetre et pour chaque périmetre un catalogue uo à respecter
class Perimetre(models.Model):
    nom=models.CharField(max_length=20)
    workPackage=models.ForeignKey(WorkPackage, 
    on_delete=models.CASCADE,
    default = "")

    def __str__(self):
        return self.nom 


    # création de niveau d'uo pour chaque uo un niveau
class Niveauuo(models.Model):
    nom=models.CharField(
        max_length=20,
    )

    def __str__(self):
       return self.nom 

# création de type d'uo pour chaque uo un type
class Typeuo(models.Model):
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom  

# création de catalogue uo et que pour chaque type et niveau un prix et un nombre de jour
class CatalogueUo(models.Model):
    nom=models.CharField(max_length=20)
    perimetre=models.ForeignKey(Perimetre, 
    on_delete=models.CASCADE,
    default = "")
    niveau=models.ForeignKey(Niveauuo, 
    on_delete=models.CASCADE,
    default = "")
    typeuo=models.ForeignKey(Typeuo, 
    on_delete=models.CASCADE,
    default = "")
    nbrjouruo=models.CharField(max_length=5)
    prixuo=models.CharField(max_length=20)

    def __str__(self):
        return self.nom   

# création de platforme et pour chaque platforme des projets differents
class Plateforme(models.Model):
    nom=models.CharField(max_length=20)
    
    def __str__(self):
       return self.nom

# création d'uet et pour chaque uet des fonctions differentes
class Uet(models.Model):
    nom=models.CharField(max_length=20) 

    def __str__(self):
       return self.nom

# création de table fonction
class Fonction(models.Model):
    nom=models.CharField(max_length=20)
    uet = models.ForeignKey(Uet,default = "",on_delete=models.CASCADE)
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
    plateforme = models.ForeignKey(Plateforme,default = "",on_delete=models.CASCADE)
    def __str__(self):
       return self.nom

class Lot(models.Model):
    nom=models.CharField(max_length=50)

    def __str__(self):
       return self.nom

# class pointage qui permet aux utilisateur de pointer sur l'uo
class Pointage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default = "")
    semaine= models.IntegerField()
    point=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5)])

    def __str__(self):
       return str(self.point)


# class note de cadrage pour chaque uo une note de cadrage 'reflichir pour apres si on peut ajouter des numero pour les modification de note de cadrage  '
class NotedeCadrage(models.Model):
    nom=models.CharField(max_length=20)
    reponseRSA=models.CharField(max_length=600,default="",blank=True, null=True)

    def __str__(self):
       return str(self.nom)


# création d'uo avec possiblité de choisir les champs dans des table differente
class Uo(models.Model):
    numuo = models.CharField(max_length=20)
    typeuo = models.ForeignKey(Typeuo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    niveauo = models.ForeignKey(Niveauuo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    projet = models.ForeignKey(Projet,default = "",on_delete=models.CASCADE,blank=True, null=True)
    fonction = models.ForeignKey(Fonction,default = "",on_delete=models.CASCADE,blank=True, null=True)
    statutuo = models.ForeignKey(Statutuo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    etatuo = models.ForeignKey(Etatuo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    plateforme = models.ForeignKey(Plateforme,default = "",on_delete=models.CASCADE,blank=True, null=True)
    uet = models.ForeignKey(Uet,default = "",on_delete=models.CASCADE,blank=True, null=True)
    catalogue = models.ForeignKey(CatalogueUo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    lot = models.ForeignKey(Lot,default = "",on_delete=models.CASCADE,blank=True)
    jalonD = models.CharField(max_length=20,default="",blank=True, null=True)
    jalonF = models.CharField(max_length=20,default="",blank=True, null=True)
    ju = models.CharField(max_length=20,default="",blank=True, null=True)
    DateDebutUO=models.DateTimeField(default=timezone.now(),blank=True, null=True)
    DateLivraison=models.DateTimeField(default=timezone.now(),blank=True, null=True)
    Client=models.CharField(max_length=20,default="",blank=True, null=True)
    avancement=models.FloatField(default=0,blank=True, null=True)
    pointage =models.ForeignKey(Pointage,on_delete=models.CASCADE,default = "",blank=True, null=True)
    piloteUo=models.CharField(max_length=20,default="",blank=True, null=True)
    notedeCadrage=models.ForeignKey(NotedeCadrage,on_delete=models.CASCADE,default = "",blank=True, null=True)
    def __str__(self):
        return self.numuo  #+ "  " + self.typeuo + "   " + self.niveauo + "   " + self.projet + "   " + self.fonction + "   " + self.platforme + "   " + self.uet


  
# classe activités pour chaque note de cadrage plusieurs activitées
class Activites(models.Model):
    notedeCadrage=models.ForeignKey(NotedeCadrage,on_delete=models.CASCADE,default = "",
                                    related_name= 'ref_cadrage')
    donnesdentree=models.CharField(max_length=600,default="")
    activiteAttendue=models.CharField(max_length=600,default="")	
    pourcentagedactivite=models.FloatField()
    Conditionsdereussite=models.CharField(max_length=600,default="")	
    Datedonnéesdentrees=models.DateTimeField(default="", blank=True)
    DatedeDemarragedActivite=models.DateTimeField( default="",blank=True)
    LivrableAttendu=models.CharField(max_length=600,default="")	
    DatedeReceptionAttenduduLivrable=models.DateTimeField(default="", blank=True)
    CommentairesSurAttendu=models.CharField(max_length=600,default="")	

    def __str__(self):
       return str(self.activiteAttendue)


    
   
##class livraison d'activité 
class Livraison(models.Model):
    nomduLivrable=models.ForeignKey(Activites,on_delete=models.CASCADE,default="")
    systèmeADAS=models.ForeignKey(Fonction,default = "",on_delete=models.CASCADE)	
    projet=models.ForeignKey(Projet,default = "",on_delete=models.CASCADE)
    jalon=models.CharField(max_length=60,default="")
    numeroUO=models.ForeignKey(Uo,on_delete=models.CASCADE,default="")
    typeuo=models.ForeignKey(Typeuo,on_delete=models.CASCADE,default="")
    niveauUO=models.ForeignKey(Niveauuo,on_delete=models.CASCADE,default="")
    pourcentagelivre=models.FloatField()
    commentaire  = models.CharField(max_length=600,default="")

    def __str__(self):
       return str(self.nomduLivrable)
