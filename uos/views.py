from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from uos.models import  Uo


def choix(objectmodel):
    liste = objectmodel.objects.all()  
    return liste
    
# Create your views here.
def uo_list(request):
    uoListe= Uo.objects.all()
    context = {
        "Uo": uoListe,
    }
    return render(request, "TableUos.html", context)


