from django.shortcuts import render, redirect, get_object_or_404
from profil.forms import RegistrationForm, EditProfileForm, EditProfileUserForm
from .models import UserProfile
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



#Affichage des information de l'utilisateur connecté 

#@login_required(login_url="connexion")
def profil(request):
    
    return render(request,'accounts/profil.html')

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
                return redirect('uo')

        else:
            messages.error(request,'Adresse mail ou mot de passe incorrect') 
            return redirect('connexion')

        return render(request,'pages/uo.html')   
    else:
        form = AuthenticationForm()
    return render(request, 'pages/connexion.html', {'form': form})   

#POUR RT : Affichage d'une liste d'utilisateur 
def user_list(request):
    userList = User.objects.all()
      
    context = {
        "user": userList, 
    }
    return render(request, "accounts/users.html", context)


      #if request.user.userprofile.role == "rt" or "chf_project":
           # else :
         #   return render(request,'pages/error404.html')

#Fonction de creation de compte UNIQUEMENT POUR RT ET +
# Ajouter la condition ci dessus pour restreindre accès a RT  
def register(request):

    

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST or None, request.FILES or None)

        
      

        if form.is_valid() and profile_form.is_valid():
            email = request.POST['email']

            user = form.save(commit=False)
            #attribution de l'adresse mail comme username (uniquement utile pour l'admin django)
            user.username = request.POST['last_name'] + ' ' +  request.POST['first_name']

            #Genere un mot de passe automatiquement
            #Reste a voir s'il faut le parametrer pour plus de difficulter ou pas
            password = User.objects.make_random_password(length=9) 

            

            user.set_password(password)
            
             

            user.save()

            user.username = request.POST['last_name'] + request.POST['first_name'] 
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()


            send_mail(
                'Votre compte a été créé',
                'Votre mdp : ' +  password,
                'Admin@expleogroup.com',
                [email],
                fail_silently=False,
            )

            return redirect('connexion')
        else:
            messages.error(request, form['first_name'].errors)
            messages.error(request, form['last_name'].errors)
            messages.error(request, form['email'].errors)
            messages.error(request, form['password1'].errors)
            messages.error(request, profile_form['poste'].errors)

    else:
        form = RegistrationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'accounts/register.html', context)


    
#Fonction modification de profile par USER sur son profile personnel
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form_profile = EditProfileUserForm(request.POST, request.FILES  or None, instance=request.user.userprofile)
       
        
        if form.is_valid() and form_profile.is_valid() :

            user_form = form.save()
            custom_form = form_profile.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('profil')
        else:
             
            
        
            messages.error(request, form['first_name'].errors)
            messages.error(request, form['last_name'].errors)
            messages.error(request, form['image'].errors)

            return redirect('edit_profile')
           
    else :
        form = EditProfileForm(instance=request.user)
        form_profile = EditProfileUserForm(instance=request.user.userprofile)

        
        args = {'form' : form, 'form_profile' : form_profile, }


        return render(request, 'accounts/edit_profile.html', args)

       


#Fonction de update user par RT : 
# !!!!!Reste a definir un accès restreint uniquement pour RT ET + !!!!!
def update_user(request, id=None):
    
    userUpdate =User.objects.get(id= id)
    
    form = EditProfileForm(request.POST or None, instance=userUpdate) 
    form_profile = EditProfileUserForm(request.POST or None,request.FILES  or None, instance=userUpdate.userprofile)    

    if form.is_valid() and form_profile.is_valid()   :

        
        userUpdate = form.save(commit=False)

        userUpdate.userprofile.save()
        userUpdate.save()
        
        return redirect('user_list')
    else : 
        messages.error(request, form_profile['image'].errors)
        
    context ={'form' : form, 'form_profile' : form_profile,}
    return render(request, "accounts/edit_profileRT.html", context)


    


#Fonction de modification de mot de passe a parir du profile User.

def change_pwd(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            adresse_mail = request.user.email
            #envoie email lorsque le mot de passe est modifié
            send_mail(
                'Votre mot de passe a étais modifié',
                'Le changement de mot de passe a étais effectué avec succès',
                'Admin@expleogroup.com',
                [adresse_mail],
                fail_silently=False,
            )
            return redirect('profil')
        else:
            return redirect('modifMdp')
    else :
        form = PasswordChangeForm(user=request.user)
        args = {'form' : form}

        return render(request, 'accounts/change_password.html', args)


