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





                                