from profil.models import Executant, Pilote
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Prend en parametre un tableau d'objet
# 1. Récupère tous les utilisateurs entrée en parametre
# 2. Récupère l'adresse mail de tous les utilisateurs
# 3. Envoie un mail à l'adresse mail pour chaque utilisateurs
def send_mail_to(array_object):
    for users in array_object:
        all_user = users.objects.all()
        for user in all_user:
            email = user.email
            print(email)
        
            send_mail(
                'Rappel pointage',
                'Veuillez effectuer vos pointages aujourd\'hui si ce n\'est pas déjà fait s\'il vous plaît.',
                'Admin@expleoWebsite.com',
                [email],
            )
    
# Instanciation de la fonction 
# Au click sur le bouton génère l'envoie de mail
def reminder_pointage(request):
    send_mail_to([Executant, Pilote])
    messages.success(request, "Les mails ont été envoyé correctement")

    return redirect('uo_list')






