from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from uos.models import *
from uos.form import *
from django.contrib import messages

from django.views import generic 
from django.views.generic.edit import CreateView


def choix(objectmodel):
    liste = objectmodel.objects.all()  
    return liste


# Create your views here.
def uo_list(request):
    uoListe= Uo.objects.all()
    context = {
        "Uo": uoListe,
    }
    return render(request, "TableUos.html", context)


class UosCreate(CreateView):
    model = Uo
    #fields = ['lot']


# fonction de création des objects
def create_fields_uo(name_niveau_uo, name_type_uo):
    Niveauuo.objects.create(nom=name_niveau_uo)
    Typeuo.objects.create(nom=name_type_uo)


def create_uo(request):

    if request.method == 'POST':
        type_uo_form = TypeUoForm(request.POST)
        niveau_uo_form = NiveauUoForm(request.POST)
        uo_principal_form = UoForm(request.POST)
        projet_form = ProjetForm(request.POST)

        print("request : ", request.POST)

        if type_uo_form.is_valid():
            type_uo_name = request.POST['nom_type_uo']
            niveau_uo_name = request.POST['nom_niveau_uo']

            number_uo = request.POST['num_uo']
            jalon_d = request.POST['jalonD']
            jalon_f = request.POST['jalonF']
            ju = request.POST['ju']
            date_uo_start = request.POST['date_debut_uo']
            date_uo_delivery = request.POST['date_livraison_uo']
            client = request.POST['client']
            avancement = request.POST['avancement']
            pilote_uo = request.POST['pilote_uo']

            # Appel de la fonction de création des objects
            create_fields_uo(niveau_uo_name, type_uo_name)

            Uo.objects.create(
                numuo = number_uo,
                jalonD = jalon_d,
                jalonF = jalon_f,
                ju = ju,
                DateDebutUO = date_uo_start,
                DateLivraison = date_uo_delivery,
                Client = client,
                avancement = avancement,
                piloteUo = pilote_uo
            )

            return redirect('create_uo')
    else:
        type_uo_form = TypeUoForm()
        niveau_uo_form = NiveauUoForm()
        uo_principal_form = UoForm()
        projet_form = ProjetForm()
    context = {
        'form_type_uo': type_uo_form,
        'form_niveau_uo': niveau_uo_form,
        'form_uo_principal': uo_principal_form,
        'form_projet': projet_form
    }

    return render(request, "create_uo.html", context)


def create_catalogue_uo(request):

    if request.method == 'POST':
        catalogue_uo_form = CatalogueForm(request.POST)

        print("request : ", request.POST)

        if catalogue_uo_form.is_valid():

            catalogue_name = request.POST['nom_catalogue']
            select_uo_type = request.POST['catalogue_select_type_uo']
            day_number = request.POST['nombre_jours_uo']
            select_uo_niveau = request.POST['catalogue_select_niveau_uo']
            price_uo = request.POST['prix_uo']

            recover_type_uo_id = Typeuo.objects.get(id = select_uo_type )
            recover_niveau_uo_id = Niveauuo.objects.get(id = select_uo_niveau )
            print("type uo : ", recover_type_uo_id)
            print("niveau uo : ", recover_niveau_uo_id )

            add_catalogue = CatalogueUo(
                nom=catalogue_name,
                nbrjouruo=day_number,
                prixuo=price_uo,
                typeuo=recover_type_uo_id,
                niveauuo=recover_niveau_uo_id,
            )
            add_catalogue.save()

            return redirect('create_catalogue_uo')
    else:
        catalogue_uo_form = CatalogueForm()

    context = {
        'form_catalogue_uo': catalogue_uo_form,

    }

    return render(request, "create_catalogue.html", context)










    



