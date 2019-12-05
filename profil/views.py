from django.shortcuts import render, redirect, get_object_or_404
from profil.forms import (
    RegistrationForm, 
    EditProfileForm, 
    EditProfileUserForm,  
    LivForm, 
    ChValidForm )
from .models import UserProfile, Liv, ChValid
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



"""
Multi-ligne commentaire avec 3 guillemets

Les prints renvoient des informations dans l'invit de commande du serveur

"""
#Affichage des information de l'utilisateur connecté 

#@login_required(login_url="connexion")
def profil(request):

    equipe_list =  Liv.objects.all().prefetch_related('executant')
    


    context = {
        "equipe": equipe_list, 
        
    }

    
    
    return render(request,'accounts/profil.html', context)

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

        equipe_form = LivForm(request.POST)

        ajout_responsable_form = ChValidForm(request.POST)
        

            

        if form.is_valid() and profile_form.is_valid() and equipe_form.is_valid and ajout_responsable_form.is_valid: 

            role = request.POST['poste']
            email = request.POST['email']
            poste = request.POST['poste']
            

            
            if 'executant' in request.POST:
            #cette condition verifie qu'un champ executant est saisi lors de l'inscription
                executant =  request.POST['executant']
               
                recup_exec = request.POST.get('executant')
                
           # return HttpResponse(str(executant))
               # if recup_exec != '':
                #    recup_user_exec = ChValid.objects.get( id = recup_exec)
                #return HttpResponse(str(recup_user_exec))
                

            #cette condition verifie qu'un champ responsable est saisi lors de l'inscription
            if 'responsable' in request.POST:
                recup_respo = request.POST.get('responsable')

                if recup_respo != '':
                    responsable = User.objects.get(liv = recup_respo)

                


            #return HttpResponse(str(responsable))
            
  

            user = form.save(commit=False)

            #attribution de l'adresse mail comme username (uniquement utile pour l'admin django)
            user.username = request.POST['last_name'] + '_' +  request.POST['first_name']

            #Genere un mot de passe automatiquement
#############RETIRER LE COMMENTAIRE CI DESSOUS######################################################
            #password = User.objects.make_random_password(length=9) 
#############LE MEME MDP POUR TOUS LES COMPTE POUR FACILITER LE DEVELOPPEMENT######################
            password = 'motdepass78'
## !!!! SUPPRIMER LE MOT DE PASSE CI DESSUS !!!!! #######
            user.set_password(password)

            user.save()

            user.username = request.POST['last_name'] + request.POST['first_name'] 

            profile = profile_form.save(commit=False)

            if role == 'liv':
                profile.role = 'pilote_activite'
            
            
            elif role == 'CH.MIL' or role == 'CH.IS' or role == 'CH.HIL'  : 
                 profile.role = 'charge_execution'

            profile.user = user
 
            profile.save()
            
            

            if poste == 'liv':
                add_executant = equipe_form.save(commit=False)
                add_executant.user= user

                add_executant.save()
        #Ajoute un executant a un responsable 
        #permet de lier deux profil dès la création d'un nouveau profil
            if 'executant' in request.POST:

                list_add_executant = request.POST.getlist('executant')
                #Ajout des nouveaux liens entre ch execuction et pilote
                for add_execut in list_add_executant:
                    print("ajout de relation avec : ")
                    print(add_execut)
            
            
                    add_executant.executant.add(add_execut)

                if recup_exec != '':
                    list_add_executant = request.POST.getlist('executant')
                    for add_execut in list_add_executant:
                        recup_user_exec = ChValid.objects.get( id = add_execut)
                        print("Ajout du liv a : ")
                        print(recup_user_exec)
                        recup_user_exec.responsable = add_executant
                        recup_user_exec.save()
                    
                    #return HttpResponse(str( "hello world"))
                
                

            if poste == 'ch.MIL' or poste == 'ch.HIL' or poste == 'ch.IS' :
            #Verifie si l'utilisateur ajouté est un chargé executant
            #Puis ajoute l'utilisateur en tant que chargé executant
            #s'il a un responsable dès la création de son compte il est lié a ce responsable
                add_responsable = ajout_responsable_form.save(commit=False)
                add_responsable.user= user

                add_responsable.save() 

                if recup_respo != '':
                #SI on choisit un responsable lors de la création du profil du ch d'execution
                #Permet de lier responsable et chargé executant ensemble 
                
                    responsable.liv.executant.add(add_responsable)

     
            send_mail(
                'Votre compte a été créé',
                'Votre mdp : ' +  password,
                'Admin@expleogroup.com',
                [email],
                fail_silently=False,
            )
            
            messages.add_message(request, messages.INFO, 'Le compte a été créer avec succès, un mail avec les informations de connexion à été envoyé a l\'adresse indiqué')
           
            return redirect('register')
        else:
            messages.error(request, form['first_name'].errors)
            messages.error(request, form['last_name'].errors)
            messages.error(request, form['email'].errors)
            messages.error(request, form['password1'].errors)
            messages.error(request, profile_form['poste'].errors)

    else:
        form = RegistrationForm()
        profile_form = UserProfileForm()
        equipe_form = LivForm()
        ajout_responsable_form = ChValidForm()
        

    context = {
        'form' : form, 
        'profile_form' : profile_form, 
        'equipe_form' : equipe_form,
        'responsable_form': ajout_responsable_form,
        
        }
    return render(request, 'accounts/register.html', context)
    


    
#Fonction modification de profile par USER sur son profile personnel
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form_profil = EditProfileUserForm(request.POST, request.FILES  or None, instance=request.user.userprofile)
       
        
        if form.is_valid() and form_profil.is_valid() :

            ## ATTRIBUTION DU USERNAME SI MODIFICATION
            user = form.save(commit=False)
            user.username = request.POST['last_name'] + '_' +  request.POST['first_name']

            user_form = form.save()
            custom_form = form_profil.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('profil')
        else:
             
            
        
            messages.error(request, form['first_name'].errors)
            messages.error(request, form['last_name'].errors)
            messages.error(request, form_profil['image'].errors)

            return redirect('edit_profile')
           
    else :
        form = EditProfileForm(instance=request.user)
        form_profil = EditProfileUserForm(instance=request.user.userprofile)

        
        args = {'form' : form, 'form_profil' : form_profil, }


        return render(request, 'accounts/edit_profile.html', args)

       


#Fonction de update user par RT : 
# !!!!!Reste a definir un accès restreint uniquement pour RT ET + !!!!!
def update_user(request, id=None):
    
    userUpdate =User.objects.get(id= id)
    
    poste = userUpdate.userprofile.poste

    if poste == 'liv':
        livUserUpdate = Liv.objects.get(user_id=id)
        #METTRE UNE CONDITION ICI EN FONCTION DU POSTE LIV CH ETC et CHANGER DE FORM
        equipe_form = LivForm(request.POST or None, instance = userUpdate.liv)
    
    form = EditProfileForm(request.POST or None, instance=userUpdate) 
    form_profil = EditProfileUserForm(request.POST or None,request.FILES  or None, instance=userUpdate.userprofile) 

    

    #ajout_responsable_form = ChValidForm(request.POST)   

    if form.is_valid() and form_profil.is_valid() :

        ## ATTRIBUTION DU USERNAME SI MODIFICATION
        user = form.save(commit=False)
        user.username = request.POST['last_name'] + '_' +  request.POST['first_name']
        
        #Suppression des liens entre ch execution et pilote
        execut = livUserUpdate.executant.all()
        print("relation supprimé avec : ")
        print(execut)
        for executant in execut : 
            livUserUpdate.executant.remove(executant)

        
        
        adresse_mail = request.POST['email']
        userUpdate = form.save(commit=False)

        userUpdate.userprofile.save()
        
        
        list_add_executant = request.POST.getlist('executant')
        #Ajout des nouveaux liens entre ch execuction et pilote
        for add_execut in list_add_executant:
            print("ajout de relation avec : ")
            print(add_execut)
            
            
            livUserUpdate.executant.add(add_execut)

        
        
        
        
        userUpdate.save()
        #SI L'UTILLISATEUR NE S'EST JAMAIS CONNECTÉ UN MAIL EST ENVOYÉ
        #METTRE CETTE CONDITION LORS DE LA MODIFICATION DE MDP PAR SUPERIEUR EN CAS D'ERREUR
        if userUpdate.last_login is None:
            send_mail(
                'Vos informations ont été modifiés',
                'Certaines de vos informations on été modifié par votre responsable',
                'Admin@expleogroup.com',
                [adresse_mail],
                fail_silently=False,
            )
        
        #return HttpResponse(str( recup_user_exec ))
        return redirect('user_list')
    else : 
        messages.error(request, form_profil['image'].errors)
    if poste == 'liv':   #ECHANGER CETTE CONDITION CONTRE UNE VARIABLE POUR equipe_form
        context ={
            'form' : form,
            'form_profil' : form_profil,
            'equipe_form_liv' : equipe_form,
            }
    else: 
        context ={
            'form' : form,
            'form_profil' : form_profil,
            
            }

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
                'Votre mot de passe à été modifié',
                'Le changement de mot de passe a été effectué avec succès',
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





def debug(request):

    respObj = ChValid.objects.first()
   # responsable = respObj.liv.get(id=19)

    
    #responsable = respObj.liv.all()
    

    responsable = User.objects.get(liv = 19)

    



    context = {
        "affiche": responsable, 
    }

    
    
    return render(request,'accounts/debug.html', context)


