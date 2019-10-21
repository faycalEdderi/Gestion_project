from django.shortcuts import render, redirect
from profil.forms import RegistrationForm, EditProfileForm, EditProfileUserForm


from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
    
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


