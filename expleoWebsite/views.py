from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def Uos(request):
    ...
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

def connexion(request):

    return render(request,'pages/connexion.html')

