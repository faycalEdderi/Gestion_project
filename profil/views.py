from django.shortcuts import render, redirect
from profil.forms import RegistrationForm 

from .forms import UserProfileForm, UserCreationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

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
