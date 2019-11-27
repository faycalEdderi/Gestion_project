from django.contrib import admin
from .models import uo , typeuo , niveauuo ,etatuo,fonction, projet, statutuo,UET , plateforme

# Register your models here.
admin.site.register(uo)
admin.site.register(typeuo)
admin.site.register(niveauuo)
admin.site.register(etatuo)
admin.site.register(fonction)
admin.site.register(plateforme)
admin.site.register(projet)
admin.site.register(statutuo)
admin.site.register(UET)