from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from profil.models import Executant, Pilote, RespTechnique,ChefdeProjet, RespSOP,Client, MyUsers
from django.utils import timezone
import django
from datetime import date
from django.contrib.messages.views import SuccessMessageMixin
from django.core.validators import RegexValidator

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
    nbr_jour_uo=models.CharField(max_length=5,)
    prix_uo=models.CharField(max_length=20)

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



# class note de cadrage pour chaque uo une note de cadrage 'reflichir pour apres si on peut ajouter des numero pour les modification de note de cadrage  '
class NotedeCadrage(models.Model):
    nom=models.CharField(max_length=20)
    reponseRSA=models.CharField(max_length=600,default="",blank=True ,null=True)

    def __str__(self):
       return str(self.nom)


# création d'uo avec possiblité de choisir les champs dans des table differente
class Uo(models.Model):
    num_uo = models.CharField(max_length=20)
    type_uo = models.ForeignKey(Typeuo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    niveau_uo = models.ForeignKey(Niveauuo,default = "",on_delete=models.CASCADE,blank=True,
                                  null=True)
    projet = models.ForeignKey(Projet,default = "",on_delete=models.CASCADE,blank=True, null=True)
    fonction = models.ForeignKey(Fonction,default = "",on_delete=models.CASCADE,blank=True, null=True)
    statut_uo = models.ForeignKey(Statutuo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    etat_uo = models.ForeignKey(Etatuo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    plateforme = models.ForeignKey(Plateforme,default = "",on_delete=models.CASCADE,blank=True, null=True)
    uet = models.ForeignKey(Uet,default = "",on_delete=models.CASCADE,blank=True, null=True)
    catalogue = models.ForeignKey(CatalogueUo,default = "",on_delete=models.CASCADE,blank=True, null=True)
    lot = models.ForeignKey(Lot,default = "",on_delete=models.CASCADE,blank=True)
    jalon_d= models.CharField(max_length=20,default="",blank=True, null=True)
    jalon_f = models.CharField(max_length=20,default="",blank=True, null=True)
    ju = models.CharField(max_length=20,default="",blank=True, null=True)
    date_debut_uo=models.DateTimeField(default=django.utils.timezone.now,blank=True, null=True)
    date_livraison=models.DateTimeField(default=django.utils.timezone.now,blank=True, null=True)
    
    note_de_cadrage=models.ForeignKey(NotedeCadrage,on_delete=models.CASCADE,default = "",blank=True, null=True)
    pilote_activitees=models.ForeignKey(Pilote,default = "",on_delete=models.CASCADE,blank=True, null=True)
    # Modifier form pour pilote qui n'est plus un charfield mais un modelfield
    client=models.ForeignKey(Client, default = "", on_delete=models.CASCADE,blank=True, null=True)
    
    #recuper ele pointage total par uo 
    @property
    def total(self):
        t=0
        for q in self.points.all():
                t+=q.point   
        return t
    #recupere le pointag  total par semaine 
    def total_semaine(self,semaine):
        t=0
        for q in self.points.filter(semaine):
                t+=q.point     
        return t
        
    #recupere avancement de chaque uo 
    @property
    def avancement(self):
        a=0
        for q in self.avancement.all():
                a=q.avancement
        return a
    
    def __str__(self):
        return self.num_uo  #+ "  " + self.typeuo + "   " + self.niveauo + "   " + self.projet + "   " + self.fonction + "   " + self.platforme + "   " + self.uet

# class pointage qui permet aux utilisateur de pointer sur l'uo
class Pointage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default = "",related_name="points")
    uo=models.ForeignKey(Uo,on_delete=models.CASCADE,default = "",related_name="points")
    semaine= models.IntegerField(default = 0)
    point=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5)])

    def __str__(self):
       return str(self.point) + str(self.uo)


# class avancement 
class Avancement(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default = "",related_name="avancement")
    uo=models.OneToOneField(Uo,on_delete=models.CASCADE,default = "",related_name="avancement")
    semaine= models.IntegerField(default = 0)
    avancement=models.FloatField()

    def __str__(self):
       return str(self.avancement)


# classe activités pour chaque note de cadrage plusieurs activitées
class Activites(models.Model):
    note_de_cadrage=models.ForeignKey(NotedeCadrage,on_delete=models.CASCADE,default = "")
    donnees_dentree=models.CharField(max_length=600,default="")
    activite_attendue = models.CharField(max_length=600,default="")	
    pourcentage_dactivite=models.FloatField()
    conditions_de_reussite=models.CharField(max_length=600,default="")	
    date_donnees_dentrees=models.DateTimeField(default="", blank=True)
    date_de_demarrage_dactivite=models.DateTimeField( default="",blank=True)
    livrable_attendu=models.CharField(max_length=600,default="")	
    date_reception_attendu_du_Livrable=models.DateTimeField(default="", blank=True)
    commentaires_sur_attendu=models.CharField(max_length=600,default="")	

    def __str__(self):
       return str(self.donnees_dentree)


    
   
##class livraison d'activité 
class Livraison(models.Model):
    nom_livrable=models.ForeignKey(Activites,on_delete=models.CASCADE,default="")
    systeme_adas=models.ForeignKey(Fonction,default = "",on_delete=models.CASCADE)	
    projet=models.ForeignKey(Projet,default = "",on_delete=models.CASCADE)
    jalon=models.CharField(max_length=60,default="")
    numero_uo=models.ForeignKey(Uo,on_delete=models.CASCADE,default="")
    type_uo=models.ForeignKey(Typeuo,on_delete=models.CASCADE,default="")
    niveau_uo=models.ForeignKey(Niveauuo,on_delete=models.CASCADE,default="")
    pourcentage_livre=models.FloatField()
    commentaire  = models.CharField(max_length=600,default="")

    def __str__(self):
       return str(self.nom_livrable)
