from profil.models import *
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
        '''
        i = 0
        while i < 5:
            User.objects.create_user(
                username="username" + str(i),
                email="user" + str(i) + "@user.com",
                password="user",
                first_name="firstname" + str(i),
                last_name="last_name" + str(i)
            )
            i += 1
        
        print("Users created")
        '''

        Role.objects.create(
            role_name="CH.EXECUTION"
        )
        Role.objects.create(
            role_name="PILOTE D'ACTIVITÉ"
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

    except:
        traceback.print_exc(file=sys.stdout)
