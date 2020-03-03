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
from django.contrib.auth.decorators import login_required

# fonction restriction d'accès
def login_exempt(view):
    view.login_exempt = True
    return view


# Class restriction accès pour user connecté
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if getattr(view_func, 'login_exempt', False):
            return

        if request.user.is_authenticated:
            return

        return login_required(view_func)(request, *view_args, **view_kwargs)


# Fonction d'affichage du profil
def display_profil(request):
    return render(request, "user_profil.html")

# Fonction d'identification
# login_exempt : acceder a cette page sans etre connecté
@login_exempt
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

            if select_poste != "" and get_new_poste == "" :
                get_poste = NewPostName.objects.get(id = select_poste )

            elif select_poste == "" and get_new_poste != "":
                get_poste = NewPostName.objects.get(post_name=get_new_poste)

            elif select_poste != "" and get_new_poste != "" :
                get_poste = NewPostName.objects.get(post_name=get_new_poste)
            else:
                get_poste = None

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

            if select_role == "3":
                new_rt = RespTechnique(
                    username=nom + "_" + prenom,
                    email=email,
                    first_name=prenom,
                    last_name=nom,
                    role=get_role,
                    poste=get_poste,
                    phone_number=phone_number
                )
                new_rt.set_password(mdp)
                new_rt.save()

            if select_role == "4":
                new_chef_projet = ChefdeProjet(
                    username=nom + "_" + prenom,
                    email=email,
                    first_name=prenom,
                    last_name=nom,
                    role=get_role,
                    poste=get_poste,
                    phone_number=phone_number
                )
                new_chef_projet.set_password(mdp)
                new_chef_projet.save()

            if select_role == "5":
                new_resp_sop = RespSOP(
                    username=nom + "_" + prenom,
                    email=email,
                    first_name=prenom,
                    last_name=nom,
                    role=get_role,
                    poste=get_poste,
                    phone_number=phone_number
                )
                new_resp_sop.set_password(mdp)
                new_resp_sop.save()
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


def edit_profil(request):
    if request.method == "POST":
        form_edit_profil = EditProfileForm(request.POST, request.FILES  or None,
                                           instance=request.user.myusers)
        print("Request : ", request.POST)
        if form_edit_profil.is_valid():

            form_edit_profil.save()

            return redirect("edit_profil")
        else:
            messages.error(request, "Erreur dans le formulaire")
            return redirect('edit_profil')
    else:
        form_edit_profil = EditProfileForm(instance=request.user.myusers)
        args = { 'form_edit_profil' : form_edit_profil }

        return render(request, 'edit_profil.html', args )


