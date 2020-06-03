from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from uos.models import *
from profil.models import *


class PlateformeResource(resources.ModelResource):
    class Meta:
        model = Plateforme


class FonctionResource(resources.ModelResource):
    uet = fields.Field(
        column_name='uet',
        attribute='uet',
        widget=ForeignKeyWidget(Uet, 'nom'))

    class Meta:
        model = Fonction


class UoResource(resources.ModelResource):

    num_uo = fields.Field(
        column_name='num_uo',
        attribute='num_uo',
    )

    type_uo = fields.Field(
        column_name='type',
        attribute='type_uo',
        widget=ForeignKeyWidget(Typeuo, 'nom'))

    niveau_uo = fields.Field(
        column_name='niveau',
        attribute='niveau_uo',
        widget=ForeignKeyWidget(Niveauuo, 'nom'))

    projet = fields.Field(
        column_name='projet',
        attribute='projet',
        widget=ForeignKeyWidget(Projet, 'nom'))

    fonction = fields.Field(
        column_name='fonction',
        attribute='fonction',
        widget=ForeignKeyWidget(Fonction, 'nom'))

    statu_uo = fields.Field(
        column_name='status',
        attribute='statut_uo',
        widget=ForeignKeyWidget(Statutuo, 'nom'))

    etat_uo = fields.Field(
        column_name='etat',
        attribute='etat_uo',
        widget=ForeignKeyWidget(Etatuo, 'nom'))

    plateforme = fields.Field(
        column_name='plateforme',
        attribute='plateforme',
        widget=ForeignKeyWidget(Plateforme, 'nom'))

    uet = fields.Field(
        column_name='uet',
        attribute='uet',
        widget=ForeignKeyWidget(Uet, 'nom'))

    catalogue = fields.Field(
        column_name='catalogue',
        attribute='catalogue',
        widget=ForeignKeyWidget(CatalogueUo, 'nom'))

    lot = fields.Field(
        column_name='lot',
        attribute='lot',
        widget=ForeignKeyWidget(Lot, 'nom'))

    jalon_d = fields.Field(
        column_name='jalon_d',
        attribute='jalon_d',
    )
    jalon_f = fields.Field(
        column_name='jalon_f',
        attribute='jalon_f',
    )

    ju = fields.Field(
        column_name='ju',
        attribute='ju',
    )

    date_debut_uo = fields.Field(
        column_name='date_debut_uo',
        attribute='date_debut_uo',
    )
    date_livraison = fields.Field(
        column_name='date_livraison',
        attribute='date_livraison',
    )

    note_de_cadrage = fields.Field(
        column_name='note de cadrage',
        attribute='note_de_cadrage',
        widget=ForeignKeyWidget(NotedeCadrage, 'nom'))

    pilote_activitees = fields.Field(
        column_name='pilote',
        attribute='pilote_activitees',
        widget=ForeignKeyWidget(Pilote, 'username'))

    client = fields.Field(
        column_name='client',
        attribute='client',
        widget=ForeignKeyWidget(Client, 'last_name'))

    class Meta:
        model = Uo
        fields = (
            'id',
            'num_uo',
            'type_uo',
            'niveau_uo',
            'projet',
            'fonction',
            'statut_uo',
            'etat_uo',
            'plateforme',
            'uet',
            'catalogue',
            'lot',
            'jalon_d',
            'jalon_f',
            'ju',
            'date_debut_uo',
            'date_livraison',
            'note_de_cadrage',
            'pilote_activitees',
            'client',
                  )
