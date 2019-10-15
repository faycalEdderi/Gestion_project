from django.shortcuts import render, redirect
from profil.forms import RegistrationForm 
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
