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

        statut_uo_list = ['Vivier', 'Cadré','En Cours',  'Livré', 'Terminé', 'Abandonné' ]
        create_obj(Statutuo, statut_uo_list)

        lot_uo_list = ['WP', 'Z']
        create_obj(Lot, lot_uo_list)


        plateform_uo_list = ['Square SUV', 'Euro6D-T','Edison', 'VU', 'CEV', 'CMFB', '1540²', 'CMF1', 'CMF1 ph1', 'CMF1 ph2']
        projet_list = ['HHN', 'X82²', 'HCC', 'HJB PHEV', 'BJA HEV', 'KFB² PHEV', 'BFB²', 'Euro6-DFull', 'HJB ICE']
        create_obj(Plateforme, plateform_uo_list)
        o =0
        while o < 9:

            get_platform = Plateforme.objects.get(nom=plateform_uo_list[o])
            Projet.objects.create(
                nom=projet_list[o],
                plateforme=get_platform
            )
            o += 1


        # valeur à changer
        etat_uo_list = ['Vivier', ' En cours Cadré',  'En cours Non Cadré', 'A temps',  'En retard',  'Terminé',  'Abandonné',  'Livré',  'Refusé']
        create_obj(Etatuo, etat_uo_list)

        uet_uo_list = ['LONGI', 'AD1', 'AWR', 'MANŒUVRE', 'LATERAL']
        fonction_list = ['AEB', 'ACC', 'AD1', 'ACC-MT', 'HFP', 'LSS 2018', 'TSR/OSP', 'HFP', 'BSW']
        create_obj(Uet, uet_uo_list)
        y = 0
        while y < 5:

            get_uet = Uet.objects.get(nom=uet_uo_list[y])
            Fonction.objects.create(
                nom=fonction_list[y],
                uet=get_uet
            )
            y += 1



        # Valeur a changer
        workpackage_uo_list = ['A', 'B', 'C', 'D', 'E', 'F']
        perimetre_list = ['BLH', 'J2J','HHL','WW', 'DLH', 'EFG']


        create_obj(WorkPackage, workpackage_uo_list)
        j = 0
        while j < 4:
            get_workpackage = WorkPackage.objects.get(nom=workpackage_uo_list[j])

            Perimetre.objects.create(
                nom = perimetre_list[j],
                workPackage =get_workpackage
            )
            j +=1

        catalogue_list = ['CATA', 'LOG', 'WORK', 'PACK', 'SIS', 'MAI']
        k=0
        while k < 4:
            get_perimetre = Perimetre.objects.get(nom=perimetre_list[k])
            get_niveau = Niveauuo.objects.get(nom=niveau_uo_list[k])
            get_type = Typeuo.objects.get(nom=type_uo_list[k])
            CatalogueUo.objects.create(
                nom=catalogue_list[k],
                perimetre=get_perimetre,
                niveau=get_niveau,
                typeuo=get_type,
                nbr_jour_uo=2,
                prix_uo=1000,
            )
            k+=1

        jalon_debut_list = ['VPC', 'TGA', 'MA', 'VPC-15s', 'ABPT1', 'SOP']
        jalon_fin_list = ['PPC', 'MA', 'VPC-15s', 'ABPT1', 'SOP+15s']


        print("Users created")
        print("Uos created")
    except NameError:
        traceback.print_exc(file=sys.stdout)
