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
import copy
from copy import deepcopy
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

        return render(request,'uos_list.html')
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})


# POUR RT PMO ou RSOP : Affichage d'une liste d'utilisateur
def user_list(request):
    if str(request.user.myusers.role) == "RT" or str(request.user.myusers.role) == "PMO" or \
            str(request.user.myusers.role) == "RSOP":

        # users_list = User.objects.all()
        users_list = User.objects.filter(is_active = True).order_by('last_name')

        context = {
            "users": users_list,
        }
        print(request.user.myusers.role)

        return render(request, "user_list.html", context)
    else :
        return  render(request, "pages/error404.html")


# Fonction de modification de mot de passe a partir du profile User.
def change_pwd(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        print("Request : ", request.POST)
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

        return render(request, 'change_password.html', args)


# Fonction de création utilisateur
def create_account(request):
    if str(request.user.myusers.role) == "RT" or str(request.user.myusers.role) == "PMO" or \
            str(request.user.myusers.role) == "RSOP":
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            form_profil = UserProfileForm(request.POST)
            form_new_poste = AjoutPosteForm(request.POST)

            print("Request : ", request.POST)
            if form_profil.is_valid():

                email = request.POST['email']
                phone_number = request.POST['phone_number']
                nom = request.POST['last_name']
                prenom = request.POST['first_name']

                select_poste = request.POST['poste']
                select_role = request.POST['role']
                get_role = Role.objects.get(id = select_role )
                get_new_poste = request.POST['post_name']

                if get_new_poste != "":
                    try:
                        NewPostName.objects.get_or_create(post_name = get_new_poste )

                    except:
                        print("Ce poste n'exste pas")

                if select_poste != "" and get_new_poste == "" :
                    get_poste = NewPostName.objects.get(id = select_poste )

                elif select_poste == "" and get_new_poste != "":
                    get_poste = NewPostName.objects.get(post_name=get_new_poste)

                elif select_poste != "" and get_new_poste != "" :
                    get_poste = NewPostName.objects.get(post_name=get_new_poste)
                else:
                    get_poste = None

                if str(get_role) == "CH.EXECUTION":
                    new_ch_execut = Executant(
                        username=nom + "_" + prenom,
                        email=email,
                        first_name=prenom,
                        last_name=nom,
                        role=get_role,
                        poste=get_poste,
                        phone_number=phone_number
                    )
                    new_ch_execut.set_password("mdp78")
                    new_ch_execut.save()

                if str(get_role) == "PILOTE_ACTIVITE":
                    new_pilote = Pilote(
                        username=nom + "_" + prenom,
                        email=email,
                        first_name=prenom,
                        last_name=nom,
                        role=get_role,
                        poste=get_poste,
                        phone_number=phone_number
                    )
                    new_pilote.set_password("mdp78")
                    new_pilote.save()

                if str(get_role) == "RT":
                    new_rt = RespTechnique(
                        username=nom + "_" + prenom,
                        email=email,
                        first_name=prenom,
                        last_name=nom,
                        role=get_role,
                        poste=get_poste,
                        phone_number=phone_number
                    )
                    new_rt.set_password("mdp78")
                    new_rt.save()

                if str(get_role) == "PMO":
                    new_chef_projet = ChefdeProjet(
                        username=nom + "_" + prenom,
                        email=email,
                        first_name=prenom,
                        last_name=nom,
                        role=get_role,
                        poste=get_poste,
                        phone_number=phone_number
                    )
                    new_chef_projet.set_password("mdp78")
                    new_chef_projet.save()

                if str(get_role) == "RSOP":
                    new_resp_sop = RespSOP(
                        username=nom + "_" + prenom,
                        email=email,
                        first_name=prenom,
                        last_name=nom,
                        role=get_role,
                        poste=get_poste,
                        phone_number=phone_number
                    )
                    new_resp_sop.set_password("mdp78")
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
    else :
        return  render(request, "pages/error404.html")


# Fonction de modification de profil par la personne elle meme
def edit_profil(request):
    if request.method == "POST":

        form_edit_profil = EditProfileForm(request.POST, request.FILES  or None,
                                           instance=request.user.myusers)
        print("Request : ", request.POST)
        if form_edit_profil.is_valid():

            form_edit_profil.save()

            return redirect("profil")
        else:
            messages.error(request, "Erreur dans le formulaire")
            return redirect('edit_profil')
    else:
        form_edit_profil = EditProfileForm(instance=request.user.myusers)
        args = { 'form_edit_profil' : form_edit_profil }

        return render(request, 'edit_profil.html', args )


# Fonction de modification de user par superieur
def update_account(request, pk=None):
    select_user_update = MyUsers.objects.get(id=pk)
    old_role = select_user_update.role
    if request.method == "POST":
        form_update_account = EditAccountForm(request.POST or None, instance=select_user_update)
        form_new_poste = AjoutPosteForm(request.POST)

        print("Request : ", request.POST)
        if form_update_account.is_valid():
            new_poste = request.POST['post_name']
            select_role = request.POST['role']
            new_role = Role.objects.get(id = select_role)

            form_update_account.save()

            if new_poste != "":
                NewPostName.objects.get_or_create(post_name = new_poste)

                select_user_update.poste = NewPostName.objects.get(post_name = new_poste )

            if new_role != old_role:
                print("add new role")

                old_obj = deepcopy(select_user_update)
                old_obj.username = str(select_user_update.username) + str(old_obj.id) +"_old"
                old_obj.is_active = False
                old_obj.id = None
                old_obj.save()

                if str(new_role) == "CH.EXECUTION":
                    check_user = Executant.objects.filter(email = select_user_update.email )
                    if not check_user:
                        new_executant = Executant(
                            username= select_user_update.username ,
                            email=old_obj.email,
                            first_name=old_obj.first_name,
                            last_name=old_obj.last_name,
                            role=old_obj.role,
                            poste=old_obj.poste,
                            phone_number=old_obj.phone_number
                        )

                        new_executant.save()
                    else:
                        find_user = Executant.objects.get(email=select_user_update.email)
                        find_user.is_active = True
                        find_user.username = select_user_update.username
                        find_user.save()

                if str(new_role) == "PILOTE_ACTIVITE":
                    check_user = Pilote.objects.filter(email=select_user_update.email)
                    if not check_user:
                        new_pilote = Pilote(
                            username=select_user_update.username,
                            email=old_obj.email,
                            first_name=old_obj.first_name,
                            last_name=old_obj.last_name,
                            role=old_obj.role,
                            poste=old_obj.poste,
                            phone_number=old_obj.phone_number
                        )
                        new_pilote.save()
                    else:
                        find_user = Pilote.objects.get(email=select_user_update.email)
                        find_user.is_active = True
                        find_user.username = select_user_update.username
                        find_user.save()

                if str(new_role) == "RT":
                    check_user = RespTechnique.objects.filter(email=select_user_update.email)
                    if not check_user:
                        new_rt = RespTechnique(
                            username=select_user_update.username,
                            email=old_obj.email,
                            first_name=old_obj.first_name,
                            last_name=old_obj.last_name,
                            role=old_obj.role,
                            poste=old_obj.poste,
                            phone_number=old_obj.phone_number
                        )
                        new_rt.save()
                    else:
                        find_user = RespTechnique.objects.get(email=select_user_update.email)
                        find_user.is_active = True
                        find_user.username = select_user_update.username
                        find_user.save()

                if str(new_role) == "PMO":
                    check_user = ChefdeProjet.objects.filter(email=select_user_update.email)
                    if not check_user:
                        new_pmo = ChefdeProjet(
                            username= select_user_update.username ,
                            email=old_obj.email,
                            first_name=old_obj.first_name,
                            last_name=old_obj.last_name,
                            role=old_obj.role,
                            poste=old_obj.poste,
                            phone_number=old_obj.phone_number
                        )
                        new_pmo.save()
                    else:
                        find_user = ChefdeProjet.objects.get(email=select_user_update.email)
                        find_user.is_active = True
                        find_user.username = select_user_update.username
                        find_user.save()

                if str(new_role) == "RSOP":
                    check_user = RespSOP.objects.filter(email=select_user_update.email)
                    if not check_user:
                        new_rsop = RespSOP(
                            username= select_user_update.username ,
                            email=old_obj.email,
                            first_name=old_obj.first_name,
                            last_name=old_obj.last_name,
                            role=old_obj.role,
                            poste=old_obj.poste,
                            phone_number=old_obj.phone_number
                        )
                        new_rsop.save()
                    else:
                        find_user = RespSOP.objects.get(email=select_user_update.email)
                        find_user.is_active = True
                        find_user.username = select_user_update.username
                        find_user.save()


                print("new_objt id : ", old_obj.id, "old_user id : ", select_user_update.id)

            #form_update_account.save()

            return redirect("user_list")
        else:
            messages.error(request, "Erreur dans le formulaire")
            return redirect('user_list')
    else:
        form_update_account = EditAccountForm(instance=select_user_update)
        form_new_poste = AjoutPosteForm()

        args = {
            'form_update_account' : form_update_account,
            'form_new_poste' : form_new_poste

        }

        return render(request, 'update_account.html', args)



