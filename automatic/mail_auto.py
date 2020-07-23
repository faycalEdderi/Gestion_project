

import schedule
import time
import datetime


date = datetime.datetime.today().weekday()

def send_rappel():

    
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
    else:
        print("This is not Friday")

def automatic():
    schedule.every().day.at("13:40").do(send_rappel)

    while True:
        schedule.run_pending()
        time.sleep(1)
