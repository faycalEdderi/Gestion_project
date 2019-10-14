from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm




def Uos(request):

    template = loader.get_template('Uos.html')
    return HttpResponse(template.render(request=request))

#def Uos(request):

    #return render(request,'Uos.html')

def profil(request):

    return render(request,'pages/profil.html')

def diagramme(request):

    return render(request,'pages/diagramme.html')

def pointages(request):

    return render(request,'pages/pointages.html')

def Uo(request):

    return render(request,'pages/Uo.html')

def historique(request):

    return render(request,'pages/historique.html')

#FONCTION LOGIN FONCTIONNELLE MAIS A AMELIORER NE PAS TOUCHER :)
def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('Uo')

        else:
            messages.error(request,'Nom d\'utilisateur ou mot de passe incorrect')  #essyeye de mettre tout en français 
            return redirect('connexion')

        return render(request,'pages/pointage.html')  #la page a renvoyé c'est celles de Uo 
    else:
        form = AuthenticationForm()
    return render(request, 'pages/connexion.html', {'form': form})   


                                