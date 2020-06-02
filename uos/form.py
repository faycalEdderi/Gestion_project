from django import forms
from profil.models import Executant, Pilote, RespTechnique,ChefdeProjet, RespSOP,Client, MyUsers
from uos.models import *
from django.forms import ModelForm


class TypeUoForm(forms.Form):
    nom_type_uo = forms.CharField(
        label="Type d'UO : ",
        required=False
    )

    class Meta:
        model = Typeuo
        fields = ['nom']


class WorkPackageForm(forms.Form):
    nom_workpackage = forms.CharField(
        label="Workpackage : ",
    )

    class Meta:
        model = WorkPackage
        fields = ['nom']


class PerimetreForm(forms.Form):
    nom_perimetre = forms.CharField(
        label="Périmètre : ",
    )
    workpackage = forms.ModelChoiceField(
        label = "Selectionner un Workpackage",
        queryset = WorkPackage.objects.all()
    )

    class Meta:
        model = Perimetre
        fields = [
            'nom',
            'workPackage'
        ]


class NiveauUoForm(forms.Form):
    nom_niveau_uo = forms.CharField(
        label="Niveau d'UO :",
        required=False
    )

    class Meta:
        model = Niveauuo
        fields = ['nom']


class ProjetForm(forms.Form):
    nom_projet = forms.CharField(
        label = "Projet : ",
        required=False
    )
    plateforme = forms.ModelChoiceField(
        label="Selectionner une plateforme",
        required = False,
        queryset=Plateforme.objects.all(),
    )

    class Meta:
        model = Projet
        fields = '__all__'


class CatalogueForm(forms.Form):
    nom_catalogue=forms.CharField(
        label="Nom Catalogue "
    )
    perimetre = forms.ModelChoiceField(
        label="Selectionner un perimetre",
        queryset=Perimetre.objects.all(),
    )
    niveau_uo = forms.ModelChoiceField(
        label="Selectionner un Niveau UO",
        queryset = Niveauuo.objects.all()
    )
    type_uo = forms.ModelChoiceField(
        label="Selectionner un Type d'UO",
        queryset = Typeuo.objects.all()
    )
    nombre_jours_uo = forms.CharField(
        label="Nombre de jours UO",
        validators=[
            RegexValidator(r'^\d{1,10}$',
                           message='Veuillez entrer un nombre de jour valide'
                           )
        ],
        error_messages = {'max_length': "Le nombre de jour le ne doit pas depasser 5 chiffres"}
    )
    prix_uo = forms.CharField(
        label="Prix de l'UO ",
        max_length=20,
        validators=[
            RegexValidator(r'^\d{1,10}$',
                           message='Veuillez saisir un prix valide'
                           )
        ],
        error_messages={'max_length': "Le prix le ne doit pas depasser 20 chiffres"}

    )

    class Meta:
        model = CatalogueUo
        fields = '__all__'


class FonctionForm(forms.Form):
    nom_fonction = forms.CharField(
        label="Fonction",
        required= False

    )
    uet = forms.ModelChoiceField(
        label = "Selectionner une UET",
        required=False,
        queryset= Uet.objects.all()
    )

    class Meta:
        model = Fonction
        fields = [
            'nom',
            'uet'
        ]


class StatutUoForm(forms.Form):
    nom_statut_uo = forms.CharField(
        label="Satut UO",
        required=False
    )

    class Meta:
        model = Statutuo
        fields = ['nom']


class EtatUoForm(forms.Form):
    nom_etat_uo = forms.CharField(
        label="Etat UO",
        required=False
    )

    class Meta:
        model = Etatuo
        fields = ['nom']


class LotUoForm(forms.Form):
    nom_lot_uo = forms.CharField(
        label="Lot UO",
        required=False
    )

    class Meta:
        model = Lot
        fields = ['nom']


class PlateformeForm(forms.Form):
    nom_plateforme = forms.CharField(
        label="Plateforme"
    )

    class Meta:
        model = Plateforme
        fields=[
            'nom',
        ]


class UetForm(forms.Form):
    nom_uet = forms.CharField(
        label="UET"
    )

    class Meta:
        model = Plateforme
        fields=[
            'nom',
            'fonction'
        ]


class UoForm(forms.ModelForm):
    num_uo = forms.CharField(
        label="Numéro de l'UO"
    )
    type_uo= forms.ModelChoiceField(
        label="Selectionner Type d'uo",
        queryset= Typeuo.objects.all()
    )
    niveau_uo = forms.ModelChoiceField(
        label="Selectionner un niveau d'uo",
        queryset=Niveauuo.objects.all()
    )
    projet = forms.ModelChoiceField(
        label="Selectionner un projet",
        queryset=Projet.objects.all(),

    )
    fonction = forms.ModelChoiceField(
        label="Selectionner une fonction",
        queryset=Fonction.objects.all(),

    )
    statut_uo = forms.ModelChoiceField(
        label="Selectionner un statut d'UO",
        queryset=Statutuo.objects.all(),

    )
    etat_uo = forms.ModelChoiceField(
        label="Selectionner un etat d'UO",
        queryset=Etatuo.objects.all(),

    )
    plateforme = forms.ModelChoiceField(
        label="Selectionner une plateform",
        queryset=Plateforme.objects.all(),

    )
    uet = forms.ModelChoiceField(
        label="Selectionner une UET",
        queryset=Uet.objects.all(),

    )
    catalogue = forms.ModelChoiceField(
        label="Selectionner un catalogue UO",
        queryset=CatalogueUo.objects.all(),

    )
    lot = forms.ModelChoiceField(
        label="Selectionner un lot",
        queryset=Lot.objects.all(),

    )
    jalon_d = forms.CharField(
        label="Jalon D",
    )
    jalon_f = forms.CharField(
        label="Jalon F",
    )
    ju = forms.CharField(
        label="JU",
    )
    date_debut_uo = forms.DateField(
        label="Date de debut UO"
    )
    date_livraison = forms.DateField(
        label="Date de livraison UO"
    )
    client = forms.ModelChoiceField(
        label="Client ",
        queryset= Client.objects.all()
    )
    pilote_activitees = forms.ModelChoiceField(
        label="Pilote UO",
        queryset= Pilote.objects.all(),
    )
    

    class Meta:
        model = Uo
        fields=(
            "num_uo",
            "type_uo",
            "niveau_uo",
            "projet",
            "fonction",
            "statut_uo",
            "etat_uo",
            "plateforme",
            "uet",
            "catalogue",
            "lot",
            "jalon_d",
            "jalon_f",
            "ju",
            "date_debut_uo",
            "date_livraison",
            "client",
            "pilote_activitees",
            "note_de_cadrage",

        )



class PointageForm(forms.Form):
    select_pilote = forms.ModelChoiceField(
        label="Selectionner un pilote",
        queryset=Pilote.objects.all(),
    )
    
    semaine = forms.IntegerField(
        label="Semaine"
    )
    point = forms.FloatField(
        label="Nombre de Jours"
    )

    class Meta:
        model = Pointage
        fields =[
            'pilote',
            'executant',
            'semaine',
            'point_pilote',
            'point_executant'
        ]
class AvancementForm(forms.Form):
    select_uo = forms.ModelChoiceField(
        label="Selectionner une UO",
        queryset=Uo.objects.all(),
    )
    
    semaine = forms.IntegerField(
        label="Semaine"
    )
    avancement = forms.FloatField(
        label="Poucentage d'avancement "
    )

    class Meta:
        model = Avancement
        fields =[
            'uo',
            'user',
            'semaine',
            'avancement'
        ]

class NoteCadrageForm(forms.Form):
  
    select_uo = forms.ModelChoiceField(
        label="Selectionner une UO",
        queryset=Uo.objects.all(),
    )
    reponse_rsa = forms.CharField(
        label="Reponse RSA" ,
        required=False
    )
    nom=forms.CharField(
        label="numero" 
    )
   

    class Meta:
        model = NotedeCadrage
        fields =[
            
            'reponseRSA',
            'nom',
        ]


class ActivitesForm(forms.Form):
    select_note_cadrage = forms.ModelChoiceField(
        label = "Selectionner note de cadrage ",
        queryset = NotedeCadrage.objects.all()
    )
    donnee_entree = forms.CharField(
        label = "Donnée entrée"
    )
    activite_attendue = forms.CharField(
        label="Activité attendue"
    )
    pourcentage_activite = forms.FloatField(
        label="Pourcentage d'activité"
    )
    conditions_reussite = forms.CharField(
        label="Condition de reussite"
    )
    date_donnee_entree = forms.DateTimeField(
        label="Date donnée d'entrée"
    )
    date_demarrage_activite = forms.DateTimeField(
        label="Date demarrage activité"
    )
    livrable_attendu = forms.CharField(
        label="livrable attendu"
    )
    date_reception_livrable = forms.DateTimeField(
        label="Date de récéption attendu du livrable"
    )
    commentaire = forms.CharField(
        label="Commentaire"
    )

    class Meta:
        model = Activites
        fields = '__all__'


class ExcelForm(forms.Form):
    import_excel = forms.FileField(
        label="Importer un fichier"
    )
