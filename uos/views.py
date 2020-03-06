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





def pointages(request):

    return render(request,'table_pointage.html')

def historique_pointage(request):

    return render(request,'table_pointage_historique.html')

# Affichage de tous les uos
def uo_list(request):
    uo_liste= Uo.objects.all()
    context = {
        "Uo": uo_liste,
    }
    return render(request, "uos_list.html", context)


def creation_uet(request):
    if request.method == 'POST':
        uet_form = UetForm(request.POST)

        print("request : ", request.POST)

        if uet_form.is_valid():

            uet_name = request.POST['nom_uet']
            select_fonction_id = request.POST['select_fonction']
            uet_select_fonction = Fonction.objects.get(id = select_fonction_id)

            create_uet = Uet(
                nom = uet_name,
                fonctions = uet_select_fonction
            )
            create_uet.save()

            return redirect('creation_uet')
    else:
        uet_form = UetForm()

    context = {
        'form_uet': uet_form,
    }

    return render(request, "create_uet.html", context)


def create_plateforme(request):

    if request.method == 'POST':
        plateforme_form = PlateformeForm(request.POST)

        print("request : ", request.POST)

        if plateforme_form.is_valid():

            plateforme_name = request.POST['nom_plateforme']
            select_projet_id = request.POST['select_projet']
            plateform_select_projet = Projet.objects.get(id = select_projet_id)

            create_plateforme = Plateforme(
                nom = plateforme_name,
                projets = plateform_select_projet
            )
            create_plateforme.save()

            return redirect('create_plateforme')
    else:
        plateforme_form = PlateformeForm()

    context = {
        'form_plateforme': plateforme_form,
    }

    return render(request, "create_plateforme.html", context)


def creation_parametre_uo(request):

    if request.method == 'POST':
        type_uo_form = TypeUoForm(request.POST)
        projet_form = ProjetForm(request.POST)
        niveau_uo_form = NiveauUoForm(request.POST)
        fonction_form = FonctionForm(request.POST)
        statut_uo_form = StatutUoForm(request.POST)
        etat_uo_form = EtatUoForm(request.POST)
        lot_uo_form = LotUoForm(request.POST)

        print("request : ", request.POST)

        if type_uo_form.is_valid():

            type_uo_name = request.POST['nom_type_uo']
            niveau_uo_name = request.POST['nom_niveau_uo']
            projet_name = request.POST['nom_projet']
            fonction_name = request.POST['nom_fonction']
            statut_uo_name = request.POST['nom_statut_uo']
            etat_uo_name = request.POST['nom_etat_uo']
            lot_uo_name = request.POST['nom_lot_uo']

            str_type_name = str(type_uo_name)
            str_niv_name = str(niveau_uo_name)
            str_projet_name = str(projet_name)
            str_fonction_name= str(fonction_name)
            str_statut_name = str(statut_uo_name)
            str_etat_name = str(etat_uo_name)
            str_lot_name = str(lot_uo_name)

            uo_type =   Typeuo( nom = type_uo_name )
            uo_niveau = Niveauuo( nom = niveau_uo_name )
            project =   Projet( nom = projet_name )
            fonction =  Fonction( nom = fonction_name)
            uo_statu =  Statutuo(nom = statut_uo_name)
            uo_state =  Etatuo(nom = etat_uo_name)
            lot =       Lot(nom = lot_uo_name)

            if str_type_name and not str_type_name.isspace():
                uo_type.save()

            if str_niv_name and not str_niv_name.isspace():
                uo_niveau.save()

            if str_projet_name and not str_projet_name.isspace():
                project.save()

            if str_fonction_name and not str_fonction_name.isspace():
                fonction.save()

            if str_statut_name and not str_statut_name.isspace():
                uo_statu.save()

            if str_etat_name and not str_etat_name.isspace():
                uo_state.save()

            if str_lot_name and not str_lot_name.isspace():
                lot.save()

            return redirect('creation_parametre_uo')
    else:
        type_uo_form = TypeUoForm()
        projet_form = ProjetForm()
        niveau_uo_form = NiveauUoForm()
        fonction_form = FonctionForm()
        statut_uo_form = StatutUoForm()
        etat_uo_form = EtatUoForm()
        lot_uo_form = LotUoForm()

    context = {
        'form_type_uo': type_uo_form,
        'form_projet': projet_form,
        'form_niveau_uo': niveau_uo_form,
        'form_fonction' : fonction_form,
        'form_statut_uo' : statut_uo_form,
        'form_etat_uo' : etat_uo_form,
        'form_lot_uo' : lot_uo_form,

    }

    return render(request, "parametre_uo.html", context)


def create_uo(request):

    if request.method == 'POST':

        uo_creation_form = UoForm(request.POST)

        print("request : ", request.POST)

        if uo_creation_form.is_valid():

            number_uo = request.POST['num_uo']
            jalon_d = request.POST['jalonD']
            jalon_f = request.POST['jalonF']
            ju = request.POST['ju']
            date_uo_start = request.POST['date_debut_uo']
            date_uo_delivery = request.POST['date_livraison_uo']
            client = request.POST['client']
            avancement = request.POST['avancement']
            pilote_uo = request.POST['pilote_uo']

            type_uo_id = request.POST['select_type_uo']
            niveau_uo_id = request.POST['select_niveau_uo']
            projet_id = request.POST['select_projet']
            fonction_id = request.POST['select_fonction']
            satut_uo_id = request.POST['select_statut_uo']
            etat_uo_id = request.POST['select_etat_uo']
            plateform_id = request.POST['select_plateform']
            uet_id = request.POST['select_uet']
            catalogue_id = request.POST['select_catalogue']
            lot_id = request.POST['select_lot']

            get_type_uo = Typeuo.objects.get(id = type_uo_id )
            get_niveau_uo = Niveauuo.objects.get(id = niveau_uo_id)
            get_projet = Projet.objects.get(id = projet_id)
            get_fonction = Fonction.objects.get(id = fonction_id )
            get_statut_uo = Statutuo.objects.get(id = satut_uo_id)
            get_etat_uo = Etatuo.objects.get(id = etat_uo_id )
            get_plateform = Plateforme.objects.get(id = plateform_id )
            get_uet = Uet.objects.get(id=uet_id)
            get_catalogue_uo = CatalogueUo.objects.get(id = catalogue_id )
            get_lot = Lot.objects.get(id = lot_id )

            create_uo = Uo(
                numuo=number_uo,
                jalonD=jalon_d,
                jalonF=jalon_f,
                ju=ju,
                DateDebutUO=date_uo_start,
                DateLivraison=date_uo_delivery,
                Client=client,
                avancement=avancement,
                piloteUo=pilote_uo,

                typeuo= get_type_uo ,
                niveauo= get_niveau_uo,
                projet= get_projet,
                fonction= get_fonction,
                statutuo= get_statut_uo,
                etatuo= get_etat_uo,
                plateforme= get_plateform,
                uet=get_uet,
                catalogue= get_catalogue_uo,
                lot=get_lot
            )
            create_uo.save()
            messages.add_message(
                request,
                messages.INFO,
                'L\'UO a etais créée correctement ')

            return redirect('uo_list')
    else:

        uo_creation_form = UoForm()

    context = {

        'form_uo_principal': uo_creation_form,

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


def create_pointage(request):

    if request.method == 'POST':
        pointage_form = PointageForm(request.POST)

        print("request : ", request.POST)

        if pointage_form.is_valid():

            selected_uo_id = request.POST['select_uo']
            selected_user_id = request.POST['select_user']
            week = request.POST['semaine']
            add_point = request.POST['point']

            recover_uo = Uo.objects.get(id = selected_uo_id )
            recover_user = User.objects.get(id=selected_user_id)

            add_pointage = Pointage(
                uo = recover_uo,
                user = recover_user,
                semaine = week,
                point = add_point
            )
            add_pointage.save()

            return redirect('create_pointage')
    else:
        pointage_form = PointageForm()

    context = {
        'form_pointage': pointage_form,

    }

    return render(request, "create_pointage.html", context)


def create_note_cadrage(request):

    if request.method == 'POST':
        note_cadrage_form = NoteCadrageForm(request.POST)

        print("request : ", request.POST)

        if note_cadrage_form.is_valid():

            selected_uo_id = request.POST['select_uo']
            answer_rsa = request.POST['reponse_rsa']

            recover_uo = Uo.objects.get(id = selected_uo_id )

            add_note_cadrage = NotedeCadrage(
                uo = recover_uo,
                reponseRSA = answer_rsa
            )
            add_note_cadrage.save()

            return redirect('create_note_cadrage')
    else:
        note_cadrage_form = NoteCadrageForm()

    context = {
        'form_note_cadrage': note_cadrage_form,

    }

    return render(request, "create_note_cadrage.html", context)


def create_activite(request):

    if request.method == 'POST':
        activite_form = ActivitesForm(request.POST)

        print("request : ", request.POST)

        if activite_form.is_valid():

            select_note_cadrage_id = request.POST['select_note_cadrage']
            data = request.POST['donnee_entree']
            activity = request.POST['activite_attendue']
            percentage = request.POST['pourcentage_activite']
            success_condition = request.POST['conditions_reussite']
            data_date = request.POST['date_donnee_entree']
            activity_start = request.POST['date_demarrage_activite']
            expected_deliverable = request.POST['livrable_attendu']
            delivery_date_available = request.POST['date_reception_livrable']
            commentary = request.POST['commentaire']

            get_note_cadrage = NotedeCadrage.objects.get(id = select_note_cadrage_id )

            add_activite = Activites(
                notedeCadrage = get_note_cadrage,
                donnesdentree = data,
                activiteAttendue = activity ,
                pourcentagedactivite = percentage ,
                Conditionsdereussite = success_condition ,
                Datedonnéesdentrees = data_date ,
                DatedeDemarragedActivite = activity_start ,
                LivrableAttendu = expected_deliverable ,
                DatedeReceptionAttenduduLivrable = delivery_date_available ,
                CommentairesSurAttendu = commentary ,

            )
            add_activite.save()

            return redirect('create_activite')
    else:
        activite_form = ActivitesForm()

    context = {
        'form_activite': activite_form,

    }

    return render(request, "create_activite.html", context)









    



