from profil.models import *
from uos.models import *
from io import *
import traceback, sys, os, random

from django.contrib.auth.models import User


def create_obj(object_name, list):
    for name in list:
        object_name.objects.create(
            nom=name
        )


def ju_creation():
     j = 0

     while j< 27 :
         print('SA'+str(j))

         j += j+5


ju_creation()


def run ():
    try:

        type_uo_list = ['PREPA', 'NUM', 'UNIT', 'SYST', 'SYNTH', 'PVAL']
        create_obj(Typeuo, type_uo_list)

        niveau_uo_list = ['A', 'B', 'C', 'D', 'E', 'F']
        create_obj(Niveauuo, niveau_uo_list)

        statut_uo_list = ['Vivier', 'Cadré', 'Abandonné', 'Livré', ]
        create_obj(Statutuo, statut_uo_list)

        lot_uo_list = ['WP', 'Z']
        create_obj(Lot, lot_uo_list)

        plateform_uo_list = ['Square SUV', 'Euro6D-T','Edison', 'VU', 'CEV', 'CMFB', '1540²', 'CMF1', 'CMF1 ph1', 'CMF1 ph2']
        projet_list = ['HHN', 'X82²', 'HCC', 'HJB PHEV', 'BJA HEV', 'KFB² PHEV', 'BFB²', 'Euro6-DFull', 'HJB ICE']
        create_obj(Plateforme, plateform_uo_list)
        for projet_name in projet_list:
            for plateforme_name in plateform_uo_list:
                get_platform = Plateforme.objects.get(nom=plateforme_name)
                Projet.objects.create(
                    nom=projet_name,
                    plateforme=get_platform
                )


        # valeur à changer
        etat_uo_list = ['A', 'B', 'C', 'D', 'E', 'F']
        create_obj(Etatuo, etat_uo_list)

        uet_uo_list = ['LONGI', 'AD1', 'AWR', 'MANŒUVRE', 'LATERAL']
        fonction_list = ['AEB', 'ACC', 'AD1', 'ACC-MT', 'HFP', 'LSS 2018', 'TSR/OSP', 'HFP', 'BSW']
        create_obj(Uet, uet_uo_list)
        for fonction_name in fonction_list:
            for uet_name in uet_uo_list :
                get_uet = Uet.objects.get(nom=uet_name)
                Fonction.objects.create(
                    nom=fonction_name,
                    uet=get_uet
                )



        # Valeur a changer
        workpackage_uo_list = ['A', 'B', 'C', 'D', 'E', 'F']
        create_obj(WorkPackage, workpackage_uo_list)

        jalon_debut_list = ['VPC', 'TGA', 'MA', 'VPC-15s', 'ABPT1', 'SOP']
        jalon_fin_list = ['PPC', 'MA', 'VPC-15s', 'ABPT1', 'SOP+15s']



        i = 0

        while i < 5:

            '''
            Pilote.objects.create(
                username="username" + str(i*125),
                email="user" + str(i*125) + "@user.fr",
                password="user",
                first_name="Prénom_pilote" + str(i*125),
                last_name="Nom_pilote" + str(i*125),
                role=pilote
            )
            Executant.objects.create(
                username="username" + str(i * 255),
                email="user" + str(i * 255) + "@user.fr",
                password="user",
                first_name="Prénom_Executant" + str(i * 255),
                last_name="Nom_Executant" + str(i * 255),
                role=executant
            )
            Client.objects.create(
                first_name="Prénom_Client" + str(i+i*125),
                last_name="Nom_Client" + str(i+i*125),
                email="user" + str(i+i*125) + "@user.fr",
                phone_number = "0654859632"
            )
            

            get_uet = Uet.objects.get(id = i)
            Fonction.objects.create(
                nom = "Fonction " + str(i),
                uet = get_uet
            )
            get_plateforme = Plateforme.objects.get(id=i)
            Projet.objects.create(
                nom="Projet " + str(i),
                plateforme=get_plateforme
            )
            get_workpackage = WorkPackage.objects.get(id=i)
            Perimetre.objects.create(
                nom="Perimetre " + str(i),
                workPackage = get_workpackage
            )
            get_perimetre = Perimetre.objects.get(id= i)
            get_type = Typeuo.objects.get(id=i)
            get_niveau = Niveauuo.objects.get(id=i)
            CatalogueUo.objects.create(
                nom = " Catalogue " + str(i),
                perimetre = get_perimetre,
                niveau = get_niveau,
                typeuo = get_type,
                nbr_jour_uo = 3 * i,
                prix_uo = 1962 * i
            )
            
            get_pilote = Pilote.objects.get( email="user" + str(i*125) + "@user.fr",)
            get_executant = Executant.objects.filter(email="user" + str(i * 255) + "@user.fr",)

            pointage = Pointage.objects.create(
                pilote=get_pilote,
                semaine="2019-01-02",
                point_pilote="4",
                point_executant="2",
            )
            pointage.executant.set(get_executant)
            NotedeCadrage.objects.create(
                nom = " Reference " + str(i),
                reponseRSA = " Reponse " + str(i)
            )
            '''
            i += 1
        print("Users created")
        print("Uos created")
    except NameError:
        traceback.print_exc(file=sys.stdout)
