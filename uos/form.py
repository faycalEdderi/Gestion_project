from django import forms
from uos.models import *


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
        required=False
    )
    select_fonction = forms.ModelChoiceField(
        label="Selectionner une fonction",
        queryset=Fonction.objects.all(),
        required=False
    )
    select_statut_uo = forms.ModelChoiceField(
        label="Selectionner un statut d'UO",
        queryset=Statutuo.objects.all(),
        required=False
    )
    select_etat_uo = forms.ModelChoiceField(
        label="Selectionner un etat d'UO",
        queryset=Etatuo.objects.all(),
        required=False
    )
    select_plateform = forms.ModelChoiceField(
        label="Selectionner une plateform",
        queryset=Plateforme.objects.all(),
        required=False
    )
    select_uet = forms.ModelChoiceField(
        label="Selectionner une UET",
        queryset=Uet.objects.all(),
        required=False
    )
    select_catalogue = forms.ModelChoiceField(
        label="Selectionner un catalogue UO",
        queryset=CatalogueUo.objects.all(),
        required=False
    )
    select_catalogue = forms.ModelChoiceField(
        label="Selectionner un catalogue UO",
        queryset=CatalogueUo.objects.all(),
        required=False
    )
    select_lot = forms.ModelChoiceField(
        label="Selectionner un lot",
        queryset=Lot.objects.all(),
        required=False
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


class TypeUoForm(forms.Form):
    nom_type_uo = forms.CharField(
        label="Type d'UO : ",
    )

    class Meta:
        model = Typeuo
        fields = ['nom']


class NiveauUoForm(forms.Form):
    nom_niveau_uo = forms.CharField(
        label="Niveau d'UO :"
    )

    class Meta:
        model = Niveauuo
        fields = ['nom']


class ProjetForm(forms.Form):
    nom_projet = forms.CharField(
        label = "Projet : "
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
