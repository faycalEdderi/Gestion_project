from django.contrib import admin
from .models import UserProfile

from .models import Rt
from .models import Liv
from .models import ChValid
#from .models import ListeDePoste
from .models import NomDePoste

admin.site.register(UserProfile)

admin.site.register(Rt)

admin.site.register(Liv)

#admin.site.register(ListeDePoste)

admin.site.register(NomDePoste)

admin.site.register(ChValid) 
