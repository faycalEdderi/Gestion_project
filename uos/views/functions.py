from django.shortcuts import render, redirect
from uos.form import *
from uos.models import *
import pandas as pd
import random
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail


# Creer, remplis un fichier excel a partir des champs d'uo
def excel_generator(request, pk=None):

    # recupere l'UO
    select_uo = Uo.objects.get(id=pk)
    if select_uo:
        # si l'uo existe recupere tous ses champs
        num_uo = select_uo.num_uo
        type_uo = select_uo.type_uo
        niveau_uo = select_uo.niveau_uo
        projet = select_uo.projet
        fonction = select_uo.fonction
        statut_uo= select_uo.statut_uo
        etat_uo= select_uo.etat_uo
        plateforme = select_uo.plateforme
        uet= select_uo.uet
        catalogue = select_uo.catalogue
        lot = select_uo.lot
        jalon_d = select_uo.jalon_d
        jalon_f = select_uo.jalon_f
        ju = select_uo.ju
        date_debut_uo = str(select_uo.date_debut_uo)
        date_livraison = str(select_uo.date_livraison)
        pilote_activitees = select_uo.pilote_activitees
        client = select_uo.client

        # Stock attribut les valeurs d'UO dans le tableau
        data = pd.DataFrame(
            {
                'Numero UO': [num_uo],
                'Type': [type_uo],
                'Niveau': [niveau_uo],
                'Projet': [projet],
                'Fonction': [fonction],
                'Statut': [statut_uo],
                'Etat': [etat_uo],
                'Plateforme': [plateforme],
                'UET': [uet],
                'Catalogue': [catalogue],
                'Lot': [lot],
                'Jalon D': [jalon_d],
                'Jalon F': [jalon_f],
                'JU': [ju],
                'Date debut': [date_debut_uo],
                'Date livraison': [date_livraison],
                'Pilote': [pilote_activitees],
                'Client': [client],
            }
        )
        # creation du fichier excel
        file_name = num_uo + str(random.randint(300,1000)) + ".xlsx"

        writer = pd.ExcelWriter(str(file_name), engine='xlsxwriter')

        # attribution des donnée dans le fichier excel
        data.to_excel(writer, sheet_name='Feuille_UO')

        # sauvegarde du fichier excel
        writer.save()

        return render(request, 'uos_list.html')

    else:
        # Si l'UO n'existe pas rajouter des messages d'erreur
        print("no uo")

