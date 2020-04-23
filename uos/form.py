from django import forms
from profil.models import Executant, Pilote, RespTechnique,ChefdeProjet, RespSOP,Client, MyUsers
from uos.models import *


class TypeUoForm(forms.Form):
    nom_type_uo = forms.CharField(
        label="Type d'UO : ",
        required=False
    )

    class Meta:
        model = Typeuo
        fields = ['nom']


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

    class Meta:
        model = Projet
        fields = '__all__'


class CatalogueForm(forms.Form):
    nom_catalogue=forms.CharField(
        label="Nom Catalogue "
    )
    catalogue_select_type_uo = forms.ModelChoiceField(
        label="Selectionner un type UO",
        queryset=Typeuo.objects.all(),
    )
    catalogue_select_niveau_uo = forms.ModelChoiceField(
        label="Selectionner un niveau UO",
        queryset=Niveauuo.objects.all(),
    )
    nombre_jours_uo = forms.CharField(
        label="Nombre de jours UO"
    )
    prix_uo = forms.CharField(
        label="Prix de l'UO "
    )

    class Meta:
        model = CatalogueUo
        fields = '__all__'


class FonctionForm(forms.Form):
    nom_fonction = forms.CharField(
        label="Fonction",
        required=False
    )

    class Meta:
        model = Fonction
        fields = ['nom']


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
    select_projet = forms.ModelChoiceField(
        label = "Selectionner un projet",
        queryset=Projet.objects.all()
    )

    class Meta:
        model = Plateforme
        fields=[
            'nom',
            'projet'
        ]


class UetForm(forms.Form):
    nom_uet = forms.CharField(
        label="UET"
    )
    select_fonction = forms.ModelChoiceField(
        label = "Selectionner une fonction",
        queryset=Fonction.objects.all()
    )

    class Meta:
        model = Plateforme
        fields=[
            'nom',
            'fonction'
        ]


class UoForm(forms.Form):
    num_uo = forms.CharField(
        label="Numéro de l'UO"
    )
    select_type_uo = forms.ModelChoiceField(
        label="Selectionner Type d'uo",
        queryset= Typeuo.objects.all()
    )
    select_niveau_uo = forms.ModelChoiceField(
        label="Selectionner un niveau d'uo",
        queryset=Niveauuo.objects.all()
    )
    select_projet = forms.ModelChoiceField(
        label="Selectionner un projet",
        queryset=Projet.objects.all(),

    )
    select_fonction = forms.ModelChoiceField(
        label="Selectionner une fonction",
        queryset=Fonction.objects.all(),
        required=False
    )
    select_statut_uo = forms.ModelChoiceField(
        label="Selectionner un statut d'UO",
        queryset=Statutuo.objects.all(),

    )
    select_etat_uo = forms.ModelChoiceField(
        label="Selectionner un etat d'UO",
        queryset=Etatuo.objects.all(),

    )
    select_plateform = forms.ModelChoiceField(
        label="Selectionner une plateform",
        queryset=Plateforme.objects.all(),

    )
    select_uet = forms.ModelChoiceField(
        label="Selectionner une UET",
        queryset=Uet.objects.all(),

    )
    select_catalogue = forms.ModelChoiceField(
        label="Selectionner un catalogue UO",
        queryset=CatalogueUo.objects.all(),

    )
    select_lot = forms.ModelChoiceField(
        label="Selectionner un lot",
        queryset=Lot.objects.all(),

    )
    jalonD = forms.CharField(
        label="Jalon D",
    )
    jalonF = forms.CharField(
        label="Jalon F",
    )
    ju = forms.CharField(
        label="JU",
    )
    date_debut_uo = forms.DateField(
        label="Date de debut UO"
    )
    date_livraison_uo = forms.DateField(
        label="Date de livraison UO"
    )
    client = forms.CharField(
        label="Client "
    )
    avancement = forms.FloatField(
        label="Avancement "
    )
    pilote_uo = forms.CharField(
        label="Pilote UO"
    )

    class Meta:
        model = Uo
        fields='__all__'


class PointageForm(forms.Form):
    select_uo = forms.ModelChoiceField(
        label="Selectionner une UO",
        queryset=Uo.objects.all(),
    )
    select_user = forms.ModelChoiceField(
        label="Selectionner un utilisateur",
        queryset=MyUsers.objects.all(),
    )
    semaine = forms.IntegerField(
        label="Semaine"
    )
    point = forms.FloatField(
        label="Nombre de points"
    )

    class Meta:
        model = Pointage
        fields =[
            'uo',
            'user',
            'semaine',
            'point'
        ]


class NoteCadrageForm(forms.Form):
    select_uo = forms.ModelChoiceField(
        label="Selectionner une UO",
        queryset=Uo.objects.all(),
    )

    reponse_rsa = forms.CharField(
        label="Reponse RSA" ,required=False
    )
    nom=forms.CharField(
        label="numero" 
    )
    class Meta:
        model = NotedeCadrage
        fields =[
            'uo',
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
        label="Donnée entrée"
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
