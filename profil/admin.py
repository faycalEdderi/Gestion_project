from django.contrib import admin
from .models import UserProfile

from .models import Rt
from .models import Liv
from .models import ChValid

admin.site.register(UserProfile)

admin.site.register(Rt)

admin.site.register(Liv)

admin.site.register(ChValid) 
