
from django.contrib import admin
from django.conf.urls import url
from .import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.conf import settings
from django.conf.urls.static import static
from profil import views as profil_views
from uos import views as uos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', uos_views.uo_list, name='uoslist'),
    path('uoslist', uos_views.uo_list, name='uoslist'),
    path('createuo', uos_views.UosCreate, name='createuo'),
    path('diagramme', views.diagramme),
    path('pointages', views.pointages, name='pointages'),
    path('uo', views.uo, name="uo"),
    path('historique', views.historique),
    

    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset_password", PasswordResetView.as_view(), name='reset_password'),
    path("reset_password/done", PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

        ##### LIEN APP PROFILE #####
    path('connexion', profil_views.connexion, name='connexion'),#Il faudra definir cette page comme page d'acceuil
    path('profil', profil_views.profil, name="profil"), 
    path('register', profil_views.register, name='register'),
    path('edit_profile', profil_views.edit_profile, name='edit_profile'),
    path('modifMdp', profil_views.change_pwd, name='modifMdp'),
    path('userList', profil_views.user_list, name='user_list'),
    path('debug', profil_views.debug, name='debug'),

    ##### LIEN APP UOS #####
    path('uo/parametres', uos_views.creation_parametre_uo, name='creation_parametre_uo'),
    path('uo/creation', uos_views.create_uo, name='create_uo'),
    path('catalogue/creation', uos_views.create_catalogue_uo, name='create_catalogue_uo'),
    path('uet/creation', uos_views.creation_uet, name='creation_uet'),
    path('plateforme/creation', uos_views.create_plateforme, name='create_plateforme'),
    
    path('user/<int:id>/update/', profil_views.update_user, name='update_user'),
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



