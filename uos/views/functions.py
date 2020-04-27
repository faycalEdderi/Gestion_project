from django.shortcuts import render, redirect
from uos.form import *
from uos.models import *
import pandas as pd
from django_pandas.io import read_frame
from django.http import HttpResponse
import random
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail


# Creer, remplis un fichier excel a partir des champs d'uo
def excel_generator(request):

    # recupere l'UO
    select_uo = Uo.objects.all()

    if select_uo:
        df = read_frame(select_uo)


        writer = pd.ExcelWriter("UO.xlsx", engine='xlsxwriter')


        # attribution des donnée dans le fichier excel
        df['date_debut_uo'] = str(df['date_debut_uo'])
        df['date_livraison'] = str(df['date_livraison'] )
        df.to_excel(writer, sheet_name='Feuille_UO')

        # sauvegarde du fichier excel
        writer.save()

        return redirect('uo_list')


    else:
        # Si l'UO n'existe pas rajouter des messages d'erreur
        print("no uo")


