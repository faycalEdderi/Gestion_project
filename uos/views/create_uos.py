from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from uos.models import *
from uos.form import *
from django.contrib import messages
from django.views import generic 
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .filters import Activitesfilter,Uosfilter,Projetfilter,Fonctionfilter,Uetfilter,Plateformefilter,Cadragefilter,Pointagefilter,Pointagefilter2
from django.db.models import Q
from django.db.models import Avg , Count, Sum
from profil.models import Executant, Pilote, RespTechnique,ChefdeProjet, RespSOP,Client, MyUsers
from django.contrib.auth import authenticate, login


def choix(objectmodel):
    liste = objectmodel.objects.all()  
    return liste


# fonction KPI 
def uo_statistique(request):
    uos = Uo.objects.all()
    total_Uos = uos.count()
    v = uos.filter(statut_uo__nom="VIVIER").count()
    l = uos.filter(statut_uo__nom="livrée").count()
    #point=Pointage.objects.annotate(sum(Pointage.point_pilote,Pointage.point_exceutant))
    context = {'uos':uos,
    'total_Uos':total_Uos ,'vivier':v
	,'livrée':l }
    return render(request, 'kpi.html', context)

def pointages(request):
    pointages= Pointage.objects.all()
    pointage_count=pointages.count()
    myFilter =Pointagefilter(request.GET, queryset=pointages)
    pointages = myFilter.qs 
    context = {
        'pointages': pointages,'pointage_count':pointage_count,
        'myFilter': myFilter
    }
    return render(request,'table_pointage.html',context)
    
def administration(request):

    return render(request,'administration.html')


def historique_pointage(request):

    return render(request,'table_pointage_historique.html')


# Affichage de tous les uos
def uo_list(request):
    uos= Uo.objects.all()
    uo_count=uos.count()
    myFilter =Uosfilter(request.GET, queryset=uos)
    uos = myFilter.qs 
    context = {
        'uos': uos,'uo_count':uo_count,
        'myFilter': myFilter
    }
    return render(request, "uos_list.html", context)

def cadrage_list(request):
    cadrages= NotedeCadrage.objects.all()
    cadrage_count=cadrages.count()
    myFilter =Cadragefilter(request.GET, queryset=cadrages)
    cadrages = myFilter.qs 
    context = {
        'cadrages': cadrages,'cadrage_count':cadrage_count,
        'myFilter': myFilter
    }
    return render(request, "notedecadrage_list.html", context)

def projet_list(request):
    projets= Projet.objects.all()
    projet_count=projets.count()
    myFilter =Projetfilter(request.GET, queryset=projets)
    projets = myFilter.qs 
    context = {
        'projets': projets,'projet_count':projet_count,
        'myFilter': myFilter
    }
    return render(request, "projet_list.html", context)

def fonction_list(request):
    fonctions= Fonction.objects.all()
    fonction_count=fonctions.count()
    myFilter =Fonctionfilter(request.GET, queryset=fonctions)
    fonctions = myFilter.qs 
    context = {
        'fonctions': fonctions,'fonction_count':fonction_count,
        'myFilter': myFilter
    }
    return render(request, "fonction_list.html", context)

def plateforme_list(request):
    plateformes= Plateforme.objects.all()
    plateforme_count=plateformes.count()
    myFilter =Fonctionfilter(request.GET, queryset=plateformes)
    plateformes = myFilter.qs 
    context = {
        'plateformes': plateformes,'plateforme_count':plateforme_count,
        'myFilter': myFilter
    }
    return render(request, "plateforme_list.html", context)

def uet_list(request):
    uets= Uet.objects.all()
    uet_count=uets.count()
    myFilter =Fonctionfilter(request.GET, queryset=uets)
    uets = myFilter.qs 
    context = {
        'uets': uets,'uet_count':uet_count,
        'myFilter': myFilter
    }
    return render(request, "uet_list.html", context)

def ActivitessList(request):
    activities = Activites.objects.all()
    activities_count = activities.count()
    myFilter = Activitesfilter(request.GET, queryset=activities)
    activities = myFilter.qs 
    context={'activities':activities,'activities_count':activities_count,
    'myFilter': myFilter}
    return render(request, 'activites_list.html',context)

#def Pointer(request):
   # pointages=Pointage.objects.all()
   # point=pointages.annotate(Sum(Ponitages.point))


def creation_uet(request):
    if request.method == 'POST':
        uet_form = UetForm(request.POST)

        print("request : ", request.POST)

        if uet_form.is_valid():

            uet_name = request.POST['nom_uet']

            create_uet = Uet(
                nom = uet_name,

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

            create_plateforme = Plateforme(
                nom = plateforme_name,
            )
            create_plateforme.save()

            return redirect('create_plateforme')
    else:
        plateforme_form = PlateformeForm()

    context = {
        'form_plateforme': plateforme_form,
    }

    return render(request, "create_plateforme.html", context)


def create_workpackage(request):

    if request.method == 'POST':
        workpackage_form = WorkPackageForm(request.POST)

        print("request : ", request.POST)

        if workpackage_form.is_valid():

            workpackage_name = request.POST['nom_workpackage']

            creation_workpackage = WorkPackage(
                nom = workpackage_name,
            )
            creation_workpackage.save()

            return redirect('create_workpackage')
    else:
        workpackage_form = WorkPackageForm()

    context = {
        'form_workpackage': workpackage_form,
    }

    return render(request, "create_workpackage.html", context)

def create_perimetre(request):

    if request.method == 'POST':
        perimetre_form = PerimetreForm(request.POST)

        print("request : ", request.POST)

        if perimetre_form.is_valid():

            perimetre_name = request.POST['nom_perimetre']
            select_workpackage = request.POST['workpackage']

            get_workpackage = WorkPackage.objects.get(id = select_workpackage)
            print("workpackage : ", get_workpackage)
            creation_workpackage = Perimetre(
                nom = perimetre_name,
                workPackage = get_workpackage
            )
            creation_workpackage.save()

            return redirect('create_perimetre')
    else:
        perimetre_form = PerimetreForm()

    context = {
        'form_perimetre': perimetre_form,
    }

    return render(request, "create_perimetre.html", context)


def creation_parametre_uo(request):

    if request.method == 'POST':
        type_uo_form = TypeUoForm(request.POST)
        niveau_uo_form = NiveauUoForm(request.POST)
        statut_uo_form = StatutUoForm(request.POST)
        etat_uo_form = EtatUoForm(request.POST)
        lot_uo_form = LotUoForm(request.POST)
        fonction_form = FonctionForm(request.POST)
        projet_form = ProjetForm(request.POST)

        print("request : ", request.POST)

        if type_uo_form.is_valid():

            type_uo_name = request.POST['nom_type_uo']
            
            niveau_uo_name = request.POST['nom_niveau_uo']
            statut_uo_name = request.POST['nom_statut_uo']
            etat_uo_name = request.POST['nom_etat_uo']
            lot_uo_name = request.POST['nom_lot_uo']
            projet_name = request.POST['nom_projet']
            fonction_name = request.POST['nom_fonction']
            select_uet = request.POST['uet']
            select_plateforme = request.POST['plateforme']

            str_type_name = str(type_uo_name)
            str_niv_name = str(niveau_uo_name)
            str_projet_name = str(projet_name)
            str_fonction_name= str(fonction_name)
            str_statut_name = str(statut_uo_name)
            str_etat_name = str(etat_uo_name)
            str_lot_name = str(lot_uo_name)

            uo_type =   Typeuo( nom = type_uo_name )
            uo_niveau = Niveauuo( nom = niveau_uo_name )
            uo_statu =  Statutuo(nom = statut_uo_name)
            uo_state =  Etatuo(nom = etat_uo_name)
            lot =       Lot(nom = lot_uo_name)

            if str_type_name and not str_type_name.isspace():
                uo_type.save()
                messages.success(request, 'Création d\'un nouveau Type UO effectué')

            if str_niv_name and not str_niv_name.isspace():
                uo_niveau.save()
                messages.success(request, 'Création d\'une nouveau Niveau UO effectué')

            if projet_name == "" and select_plateforme != "":

                messages.error(request, 'Veuillez saisir un Projet.')

            if str_projet_name and not str_projet_name.isspace():

                if select_plateforme != "":
                    get_plateforme = Plateforme.objects.get(id=select_plateforme)
                    project = Projet(
                        nom=projet_name,
                        plateforme=get_plateforme
                    )
                    project.save()
                    messages.success(request, 'Création d\'une nouvelle Plateforme effectué')
                else:
                    messages.error(request, 'Veuillez selectionner une plateforme.')

            if fonction_name == "" and select_uet != "":

                messages.error(request, 'Veuillez saisir une Fonction.')

            if str_fonction_name and not str_fonction_name.isspace():
                if select_uet != "":
                    get_uet = Uet.objects.get(id=select_uet)

                    fonction = Fonction(
                        nom=fonction_name,
                        uet = get_uet
                    )

                    fonction.save()
                    messages.success(request, 'Création d\'une nouvelle UET effectué')
                else:
                    messages.error(request,'Veuillez selectionner une UET.')

            if str_statut_name and not str_statut_name.isspace():
                uo_statu.save()
                messages.success(request, 'Création d\'un nouveau statut d\'UO effectué')

            if str_etat_name and not str_etat_name.isspace():
                uo_state.save()
                messages.success(request, 'Création d\'un nouvel Etat d\'UO effectuée')

            if str_lot_name and not str_lot_name.isspace():
                lot.save()
                messages.success(request, 'Création d\'un nouveau Lot effectuée')

            return redirect('creation_parametre_uo')
    else:
        type_uo_form = TypeUoForm()
        fonction_form = FonctionForm()
        niveau_uo_form = NiveauUoForm()
        projet_form = ProjetForm()
        statut_uo_form = StatutUoForm()
        etat_uo_form = EtatUoForm()
        lot_uo_form = LotUoForm()
        
       

    context = {
        'form_type_uo': type_uo_form,
        'form_projet': projet_form,
        'form_fonction' : fonction_form,
        'form_niveau_uo': niveau_uo_form,
      
        'form_statut_uo' : statut_uo_form,
        'form_etat_uo' : etat_uo_form,
        'form_lot_uo' : lot_uo_form,

    }

    return render(request, "parametre_uo.html", context)


def find_object(object_name, pk):
    find_obj = object_name.objects.get(id = pk )
    return find_obj


def create_uo(request):

    if request.method == 'POST':

        uo_creation_form = UoForm(request.POST)

        print("request : ", request.POST)

        if uo_creation_form.is_valid():

            number_uo = request.POST['num_uo']
            jalon_d = request.POST['jalon_d']
            jalon_f = request.POST['jalon_f']
            ju = request.POST['ju']
            date_uo_start = request.POST['date_debut_uo']
            date_uo_delivery = request.POST['date_livraison']


            type_uo_id = request.POST['type_uo']
            niveau_uo_id = request.POST['niveau_uo']
            projet_id = request.POST['projet']
            fonction_id = request.POST['fonction']
            satut_uo_id = request.POST['statut_uo']
            etat_uo_id = request.POST['etat_uo']
            plateform_id = request.POST['plateforme']
            uet_id = request.POST['uet']
            catalogue_id = request.POST['catalogue']
            lot_id = request.POST['lot']

            client_id = request.POST['client']
          
            pilote_id = request.POST['pilote_activitees']
            

            result = find_object(Typeuo, type_uo_id)
            print("object : ", result)

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

            get_pilote = Pilote.objects.get(id=pilote_id)
            get_client = Client.objects.get(id=client_id)
           
            
            create_uo = Uo(
                num_uo=number_uo,
                jalon_d=jalon_d,
                jalon_f=jalon_f,
                ju=ju,
                date_debut_uo=date_uo_start,
                date_livraison=date_uo_delivery,
                type_uo= get_type_uo ,
                niveau_uo= get_niveau_uo,
                projet= get_projet,
                fonction= get_fonction,
                statut_uo= get_statut_uo,
                etat_uo= get_etat_uo,
                plateforme= get_plateform,
                uet=get_uet,
                catalogue= get_catalogue_uo,
                lot=get_lot,
                pilote_activitees=get_pilote,
                client=get_client,
            )
            create_uo.save()

            messages.add_message(
                request,
                messages.INFO,
                'L\'UO a etais créée correctement ')

            return redirect('uo_list')
        else:
            print("error")
            messages.error(request, form.errors)
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
            select_uo_type = request.POST['type_uo']
            day_number = request.POST['nombre_jours_uo']
            select_uo_niveau = request.POST['niveau_uo']
            price_uo = request.POST['prix_uo']
            select_perimetre = request.POST['perimetre']

            get_perimetre = Perimetre.objects.get(id = select_perimetre)
            recover_type_uo_id = Typeuo.objects.get(id = select_uo_type )
            recover_niveau_uo_id = Niveauuo.objects.get(id = select_uo_niveau )
            print("type uo : ", recover_type_uo_id)
            print("niveau uo : ", recover_niveau_uo_id )

            add_catalogue = CatalogueUo(
                nom=catalogue_name,
                perimetre = get_perimetre,
                niveau=recover_niveau_uo_id,
                typeuo=recover_type_uo_id,
                nbr_jour_uo=day_number,
                prix_uo=price_uo,
            )
            add_catalogue.save()
            messages.success(request, 'Création d\'un nouveau Catalogue effectué')

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
            week = request.POST['semaine']
            add_point_pil = request.POST['point_pilote']
            add_point_exec = request.POST['point_executant']

            recover_uo = Uo.objects.get(id = selected_uo_id )
            recover_user = request.user
            
            add_pointage = Pointage(
                uo = recover_uo,
                user = recover_user,
                semaine = week,
                point = add_point
            )
            pointage.executant.set(get_executant)


            return redirect('create_pointage')
    else:
        pointage_form = PointageForm()

    context = {
        'form_pointage': pointage_form,

    }

    return render(request, "create_pointage.html", context)


#creation d'avancement
def create_avancement(request):

    if request.method == 'POST':
        avancement_form = AvancementForm(request.POST)

        print("request : ", request.POST)

        if avancement_form.is_valid():

            selected_uo_id = request.POST['select_uo']
            week = request.POST['semaine']
            add_avc = request.POST['avancement']

            recover_uo = Uo.objects.get(id = selected_uo_id )
            recover_user = request.user
            
            add_avancement = Avancement(
                uo = recover_uo,
                user = recover_user,
                semaine = week,
                avancement = add_avc
            )
            add_avancement.save()

            return redirect('create_avancement')
    else:
        avancement_form = AvancementForm()

    context = {
        'form_avancement': avancement_form,

    }

    return render(request, "create_avancement.html", context)

def create_note_cadrage(request):

    if request.method == 'POST':
        note_cadrage_form = NoteCadrageForm(request.POST)


        print("request : ", request.POST)

        if note_cadrage_form.is_valid():

            
            selected_uo_id = request.POST['select_uo']
            answer_rsa = request.POST['reponse_rsa']
            nom=request.POST['nom']
 
            recover_uo = Uo.objects.get(id = selected_uo_id )

            add_note_cadrage = NotedeCadrage(
                uo = recover_uo,
                reponseRSA = answer_rsa,
                nom=nom
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

            add_activite= Activites(
                note_de_cadrage = get_note_cadrage,
                donnees_dentree = data,
                activite_attendue = activity ,
                pourcentage_dactivite = percentage ,
                conditions_de_reussite = success_condition ,
                date_donnees_dentrees = data_date ,
                date_de_demarrage_dactivite = activity_start ,
                livrable_attendu = expected_deliverable ,
                date_reception_attendu_du_Livrable = delivery_date_available ,
                commentaires_sur_attendu = commentary ,
            )
            add_activite.save()

            return redirect('activitelist')
    else:
        activite_form = ActivitesForm()

    context = {
        'form_activite': activite_form,

    }

    return render(request, "create_activite.html", context)




def ActivitessList(request):
    activities = Activites.objects.all()
    activities_count = activities.count()
    myFilter = Activitesfilter(request.GET, queryset=activities)
    activities = myFilter.qs 
    context={'activities':activities,'activities_count':activities_count,
    'myFilter': myFilter}
    return render(request, 'activites_list.html',context)







        



