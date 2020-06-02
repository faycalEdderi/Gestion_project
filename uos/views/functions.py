from django.shortcuts import render, redirect
from uos.form import *
from uos.models import *
import pandas as pd
from django_pandas.io import read_frame
from tablib import Dataset
from .excel_resources import *
from django.http import HttpResponse
import random
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect




# Creer, remplis et exporte un fichier excel a partir des champs d'uo
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


# Importation de fichier  excel

def excel_import(request):
    if request.method == 'POST':
        #plateforme = PlateformeResource()
        #fonction = FonctionResource()

        print("Request", request)
        uo_ressource = UoResource()

        dataset = Dataset()
        new_import = request.FILES['excel_file']

        imported_data = dataset.load(new_import.read())
        result = uo_ressource.import_data(dataset, dry_run=True, raise_errors=True) # Test the data import

        if not result.has_errors():
            uo_ressource.import_data(dataset, dry_run=False) # Actually import now

    return render(request, 'excel/import.html')


