from profil.models import *
import traceback, sys, os, random
import bcrypt


def run ():
    try:
        def create_user():

            list_prenom = [ 'Jean', 'Benoit', 'Marie', 'Mohamed', 'Mariam', 'Mark',
                            'Lucie', 'Vincent', 'Florian', 'Gurvan', 'Louis', 'Axel', 'Aymeric',
                            'Morgan', 'Julien', 'Sebastien', 'Axelle', 'Maliel', 'Juliette', 'Julie',
                            'Benedict', 'Samira', 'Sam', 'Loubna', 'Mamadou', 'Hans', 'Jefferson',
                            'Haoze', 'Hu', 'Sioban', 'Akira', 'Lang', 'Abdoulay', 'Ibrahim', 'Aïssa']

            list_nom = [ 'Dubost', 'Arya', 'Vieu', 'Vital', 'Vouchet', 'Lam', 'Kotoev', 'Habal',
                         'Ezekiel', 'Amaza', 'Jegou', 'Bouchet', 'Ba', 'Flam', 'Liam', 'Mathieu',
                         'Marx', 'Hugo', 'Momonuske', 'Brill', 'Fouez', 'Mach', 'Cena', 'Vinsmoke',
                         'Ayara', 'Kari', 'Chkirat', 'Kaouas', 'Kuoch', 'Ndiay', 'Fall', 'Tan',
                         'Séddoune', 'Hichak', 'Dubois']

            User.objects.create_superuser(
                'fayçal',
                'faycal.edderi@expleogroup.com',
                'tfsbea94'
            )
            print("Superuser created")

            Role.objects.create(role_name="CH.EXECUTION")
            Role.objects.create(role_name="PILOTE_ACTIVITE")
            Role.objects.create(role_name="RT")
            Role.objects.create(role_name="PMO")
            Role.objects.create(role_name="RSOP")
            rt = Role.objects.get(role_name="RT")
            pilote = Role.objects.get(role_name="PILOTE_ACTIVITE")
            executant = Role.objects.get(role_name="CH.EXECUTION")
            print("Roles created")

            rt = Role.objects.get(role_name="RT")
            MyUsers.objects.create_user(
                username="user",
                email="user@email.com",
                password="user",
                first_name="user_prenom",
                last_name="user_nom",
                role=rt
            )
            i = 0
            while i < 5:
                Client.objects.create(

                    first_name = random.choice(list_prenom),
                    last_name = random.choice(list_nom),
                    email = "email" + str(i) + "@live.fr",
                )
                Pilote.objects.create(
                    username="username" + str(i * 125),
                    email="user" + str(i * 125) + "@user.fr",
                    password="user",
                    first_name=random.choice(list_prenom),
                    last_name=random.choice(list_nom),
                    role=pilote
                )
                Executant.objects.create(
                    username="username" + str(i+1),
                    email="user" + str(i * 4) + "@user.fr",
                    password="user",
                    first_name=random.choice(list_prenom),
                    last_name=random.choice(list_nom),
                    role=executant
                )
                i += 1

            def creation_users(object, user_role):
                object.objects.create(
                    username=username,
                    email=adresse_mail,
                    password=hashed,
                    first_name=prenom,
                    last_name=nom,
                    role=user_role
                )
                return username

            for user in list_nom:

                prenom = random.choice(list_prenom)
                nom = random.choice(list_nom)
                username = nom + "_" + prenom
                adresse_mail = nom.lower() + "." + prenom.lower() + "@expleogroup.com"
                password = b'user'
                hashed = bcrypt.hashpw(password, bcrypt.gensalt())

                print(prenom)
                print(nom)
                print(username)
                print(adresse_mail)

                check_user = User.objects.filter(username=username)
                if not check_user:
                    creation_users(MyUsers, rt)


                else:
                    continue

            return prenom, nom, username, adresse_mail, hashed

        create_user()

    except NameError:
        traceback.print_exc(file=sys.stdout)
