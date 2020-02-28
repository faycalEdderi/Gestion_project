from django.shortcuts import render, redirect, get_object_or_404
from profil.forms import *
from .models import *
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib import messages
from django import forms
import random
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


#Fonction de connection
def connexion(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('uoslist')

        else:
            messages.error(request,'Adresse mail ou mot de passe incorrect') 
            return redirect('connexion')

        return render(request,'pages/uo.html')   
    else:
        form = AuthenticationForm()
    return render(request, 'pages/connexion.html', {'form': form})   

# POUR RT : Affichage d'une liste d'utilisateur
def user_list(request):
    userList = User.objects.all()
      
    context = {
        "user": userList, 
    }
    return render(request, "user_list.html", context)


# @login_required(login_url="connexion")
def profil(request):

    return render(request, 'user_profil.html')



# Fonction de modification de mot de passe a partir du profile User.

def change_pwd(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            adresse_mail = request.user.email
            # envoie email lorsque le mot de passe est modifié
            send_mail(
                'Votre mot de passe à été modifié',
                'Le changement de mot de passe a été effectué avec succès',
                'Admin@expleogroup.com',
                [adresse_mail],
                fail_silently=False,
            )
            return redirect('profil')
        else:
            return redirect('modifMdp')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form' : form}

        return render(request, 'accounts/change_password.html', args)


# Fonction de création utilisateur
# Fonction de création utilisateurs
def create_account(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form_profil = UserProfileForm(request.POST)
        form_new_poste = AjoutPosteForm(request.POST)

        print("Request : ", request.POST)
        if form_profil.is_valid():
            print("form is valid")
            email = request.POST['email']
            phone_number = request.POST['phone']
            nom = request.POST['last_name']
            prenom = request.POST['first_name']

            mdp = "motdepasse78"

            select_poste = request.POST['poste']
            select_role = request.POST['role']
            get_role = Role.objects.get(id = select_role )

            get_new_poste = request.POST['post_name']
            if get_new_poste != "":

                new_poste = NewPostName(
                    post_name=get_new_poste
                )
                new_poste.save()
            else:
                new_poste = None

            if select_poste != "" or new_poste == "":
                get_poste = NewPostName.objects.get(id = select_poste )
            else:
                get_poste = NewPostName.objects.get(post_name = get_new_poste )

            if select_role == "1":
                new_ch_execut = Executant(
                    username=nom + "_" + prenom,
                    email=email,
                    first_name=prenom,
                    last_name=nom,
                    role=get_role,
                    poste=get_poste,
                    phone_number=phone_number
                )
                new_ch_execut.set_password(mdp)
                new_ch_execut.save()
                
            if select_role == "2":
                new_pilote = Pilote(
                    username=nom + "_" + prenom,
                    email=email,
                    first_name=prenom,
                    last_name=nom,
                    role=get_role,
                    poste=get_poste,
                    phone_number=phone_number
                )
                new_pilote.set_password(mdp)
                new_pilote.save()
            '''
            send_mail(
                'Votre compte a été créé',
                'Votre mdp : ' + mdp,
                'Admin@expleogroup.com',
                [email],
                fail_silently=False,
            )
            '''
            return redirect('create_account')
        else:
            messages.error(request, "Error")
            return redirect('create_account')

    else:
        form = RegistrationForm()
        form_profil = UserProfileForm()
        form_new_poste = AjoutPosteForm()

        args = {
            'form_user': form,
            'form_profil': form_profil,
            'form_new_poste': form_new_poste,

        }

        return render(request, 'create_user.html', args)
