
from django.contrib import admin
from django.conf.urls import url
from .import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from profil import views as profil_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Uos),
    path('profil', views.profil),
    path('diagramme', views.diagramme),
    path('pointages', views.pointages, name='pointages'),
    path('Uo', views.Uo, name="Uo"),
    path('historique', views.historique),
    path('connexion', views.connexion, name='connexion'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register', profil_views.register, name='register'),
]
