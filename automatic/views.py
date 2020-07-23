import datetime
from django.shortcuts import redirect

# Fonction d'envoi de mail chaque vendredi
def check_date():
    date = datetime.datetime.today().weekday()
    if date == 4:
        print("this is Friday")
        '''
        send_mail(
                "RAPPEL POINTAGE",
                "N'oubliez pas d'effectuer vos pointages avant 12h",
                'Admin@expleogroup.com',
                [adresse_mail],
                fail_silently=False,
            )
        '''
        return redirect('uo_list')
    else:
        print("This is not Friday")