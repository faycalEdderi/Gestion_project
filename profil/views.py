
from django.shortcuts import render, redirect, get_object_or_404
from profil.forms import RegistrationForm, EditProfileForm, EditProfileUserForm
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib import messages




def user_list(request):
    userList = User.objects.all()
    

    context = {
        "user": userList
    }
    return render(request, "accounts/users.html", context)
    
    
      #if request.user.userprofile.role == "rt":
           # else :
         #   return render(request,'pages/error404.html')

  #Fonction de creation de compte UIQUEMENT POUR RT ET +
  # Ajouter la condition ci dessus pour restreindre accès a RT  
def register(request):
   

    if request.method == 'POST':
        form = RegistrationForm(request.POST,)
        profile_form = UserProfileForm(request.POST or None, request.FILES or None)

        if form.is_valid() and profile_form.is_valid():

            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            return redirect('connexion')
        else:
            messages.error(request, form['first_name'].errors)
            messages.error(request, form['last_name'].errors)
            messages.error(request, form['email'].errors)
            messages.error(request, form['password1'].errors)
            
    else:
        form = RegistrationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'accounts/register.html', context)


    
#Fonctin modification de profile par USER sur son profil personnel
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
    context ={'form' : form, 'form_profile' : form_profile,}
    return render(request, "accounts/edit_profileRT.html", context)


    


#Fonction de modification de mot de passe a parir du profil User.

def change_pwd(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profil')
        else:
            return redirect('modifMdp')
    else :
        form = PasswordChangeForm(user=request.user)
        args = {'form' : form}

        return render(request, 'accounts/edit_profile.html', args)


