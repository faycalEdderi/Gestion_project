from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from uos.models import  Uo
from django.views import generic 
from django.views.generic.edit import CreateView

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



#class DetailUO(generic.DetailView):
    #template_name='TableUos.html'
    #model = Uo
    
    #def get_queryset(self):
       #return Uo.object.all()

class UosCreate(CreateView):
    model = Uo
    #fields = ['lot']







    



