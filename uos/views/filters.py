import django_filters 
from uos.models import *


class   Activitesfilter(django_filters.FilterSet):
    class Meta:
        model =  Activites
        fields=['note_de_cadrage']


class Uosfilter(django_filters.FilterSet):
    class Meta:
        model =  Uo
        fields=['num_uo','statut_uo','projet']


class Projetfilter(django_filters.FilterSet):
    class Meta:
        model =  Projet
        fields=['nom']

class Fonctionfilter(django_filters.FilterSet):
    class Meta:
        model =  Fonction
        fields=['nom']

class Uetfilter(django_filters.FilterSet):
    class Meta:
        model = Uet
        fields=['nom']

class Plateformefilter(django_filters.FilterSet):
    class Meta:
        model = Plateforme
        fields=['nom']

class Cadragefilter(django_filters.FilterSet):
    class Meta:
        model = NotedeCadrage
        fields=['nom']


class Pointagefilter(django_filters.FilterSet):
    class Meta:
        model = Pointage
        fields=['user','semaine','uo','uo__projet']

class Pointagefilter2(django_filters.FilterSet):
    class Meta:
        model = Pointage
        fields=['uo']      