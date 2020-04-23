from django.shortcuts import render, redirect
from uos.form import *
from uos.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail


def update_uos(request, pk=None):
    select_uo = Uo.objects.get(id=pk)
    if request.method == "POST":
        uo_update_form = UoForm(request.POST or None, instance=select_uo)
        print("Request : ", request.POST)

        if uo_update_form.is_valid():
            uo_update_form.save()
            return redirect("uo_list")
        else:
            messages.error(request, "Erreur dans le formulaire")
            return redirect("uo_list")
    else:
        uo_update_form = UoForm(instance=select_uo)
        uo_liste = Uo.objects.get(id=pk)
        context = {
            "uo": uo_liste,
            'form_update_uo': uo_update_form
        }

    return render(request, 'update_uo.html', context)







