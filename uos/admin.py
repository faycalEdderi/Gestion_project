from django.contrib import admin
from .models import Uo, Typeuo , Niveauuo ,Etatuo,Fonction, Projet, Statutuo,Uet , Plateforme ,WorkPackage,Perimetre,CatalogueUo , Pointage , Lot ,Activites,NotedeCadrage
# Register your models here.
admin.site.register(Uo)
admin.site.register(Typeuo)
admin.site.register(Niveauuo)
admin.site.register(Etatuo)
admin.site.register(Fonction)
admin.site.register(Plateforme)
admin.site.register(Projet)
admin.site.register(Statutuo)
admin.site.register(Uet)
admin.site.register(CatalogueUo)
admin.site.register(Perimetre)
admin.site.register(Pointage)
admin.site.register(WorkPackage)
admin.site.register(Lot)
admin.site.register(Activites)
admin.site.register(NotedeCadrage)