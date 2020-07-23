from profil.models import RespTechnique
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

def reminder_pointage(request):
    all_rt = RespTechnique.objects.all()
    for rt in all_rt:
        email = rt.email
        print(email)
    
        send_mail(
            'Subject',
            'Message.',
            'Admin@expleoWebsite.com',
            [email],
        )

    return redirect('uo_list')
