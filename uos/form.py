from django import forms
from uos.models import *


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
    client = forms.ModelChoiceField(
        label="Client ",
        queryset= Client.objects.all()
    )
    avancement = forms.FloatField(
        label="Avancement "
    )
    pilote_uo = forms.ModelChoiceField(
        label="Pilote UO",
        queryset= Pilote.objects.all(),
    )
    pointage = forms.ModelChoiceField(
        label = "Pointage : ",
        queryset = Pointage.objects.all()
    )
    note_cadrage = forms.ModelChoiceField(
        label="Note de cadrage : ",
        queryset = NotedeCadrage.objects.all()
    )

    class Meta:
        model = Uo
        fields='__all__'


class PointageForm(forms.Form):
    select_pilote = forms.ModelChoiceField(
        label="Selectionner une UO",
        queryset=Pilote.objects.all(),
    )
    select_executant = forms.ModelMultipleChoiceField(
        label="Selectionner un utilisateur",
        queryset=Executant.objects.all(),
    )
    semaine = forms.DateTimeField(
        label="Semaine"
    )
    point_pilote = forms.FloatField(
        label="Nombre de points pilote"
    )
    point_executant = forms.FloatField(
        label="Nombre de points executant"
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


class NoteCadrageForm(forms.Form):
    nom_cadrage = forms.CharField(
        label="Entrer reference note de cadrage",
    )

    reponse_rsa = forms.CharField(
        label="Reponse RSA",
        required=False,
    )
    select_activite = forms.ModelMultipleChoiceField(
        label="Selectionner activité ",
        queryset=Activites.objects.all()
    )

    class Meta:
        model = Pointage
        fields =[
            'nom_cadrage',
            'reponseRSA',
            'select_activite',
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
