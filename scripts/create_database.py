from profil.models import *
from uos.models import *
import traceback, sys
from django.contrib.auth.models import User


def run ():
    try:
        User.objects.create_superuser(
            'fayçal',
            'faycal.edderi@expleogroup.com',
            'tfsbea94'
        )
        print("Superuser created")

        Role.objects.create(
            role_name="CH.EXECUTION"
        )
        Role.objects.create(
            role_name="PILOTE_ACTIVITE"
        )
        Role.objects.create(
            role_name="RT"
        )
        Role.objects.create(
            role_name="PMO"
        )
        Role.objects.create(
            role_name="RSOP"
        )
        print("Roles created")

        i = 1
        rt = Role.objects.get(id=3)
        while i < 5:
            MyUsers.objects.create_user(
                username="username" + str(i),
                email="user" + str(i) + "@user.fr",
                password="user",
                first_name="firstname" + str(i),
                last_name="last_name" + str(i),
                role=rt
            )


            Typeuo.objects.create(
               nom = "Type UO " + str(i)
            )
            Niveauuo.objects.create(
                nom="Niveau UO " + str(i)
            )
            Statutuo.objects.create(
                nom="Statut UO " + str(i)
            )
            Lot.objects.create(
                nom="Lot UO " + str(i)
            )
            Etatuo.objects.create(
                nom="Etat UO " + str(i)
            )
            Plateforme.objects.create(
                nom="Plateform UO " + str(i)
            )
            Uet.objects.create(
                nom="Uet UO " + str(i)
            )
            WorkPackage.objects.create(
                nom="Workpackage " + str(i)
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
            i += 1
        print("Users created")
        print("Uos created")
    except NameError:
        traceback.print_exc(file=sys.stdout)
