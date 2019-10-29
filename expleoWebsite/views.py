from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required




def theme(request):

    template = loader.get_template('theme.html')
    return HttpResponse(template.render(request=request))




#@login_required(login_url="connexion")
def profil(request):
    
    return render(request,'pages/profil.html')

def diagramme(request):

    return render(request,'pages/diagramme.html')

def pointages(request):

    return render(request,'pages/pointages.html')

def uo(request):
   # if request.user.userprofile.role == "rt":
        return render(request,'pages/uo.html')
    #else :
    #    return render(request,'pages/error404.html')

def historique(request):

    return render(request,'pages/historique.html')


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


                                