
from django.shortcuts import render, redirect, get_object_or_404
from profil.forms import RegistrationForm, EditProfileForm, EditProfileUserForm
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, get_user_model




def user_list(request):
    userList = User.objects.all()
    

    context = {
        "user": userList
    }
    return render(request, "accounts/users.html", context)
    
    
      #if request.user.userprofile.role == "rt":
           # else :
         #   return render(request,'pages/error404.html')
    
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
        form = RegistrationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'accounts/register.html', context)


    

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
    else :
        form = EditProfileForm(instance=request.user)
        form_profile = EditProfileUserForm(instance=request.user.userprofile)

        
        args = {'form' : form, 'form_profile' : form_profile, }


        return render(request, 'accounts/edit_profile.html', args)



def update_user(request, id=None):
    userUpdate =User.objects.get(id= id)
    form = EditProfileForm(request.POST or None, instance=userUpdate)    
    if form.is_valid()   :

        userUpdate = form.save(commit=False)
        userUpdate.save()
        return redirect('user_list')
  
    context ={'form' : form}
    return render(request, "accounts/edit_profile.html", context)
    




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


