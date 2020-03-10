
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
    path('uos/list', uos_views.uo_list, name='uoslist'),
    path('diagramme', views.diagramme),


    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset_password", PasswordResetView.as_view(), name='reset_password'),
    path("reset_password/done", PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

        ##### LIEN APP PROFILE #####
    path('connexion', profil_views.connexion, name='connexion'),#Il faudra definir cette page comme page d'acceuil
    path('profil', profil_views.display_profil, name="profil"),
    path('change/mdp', profil_views.change_pwd, name='modifMdp'),
    path('users/list', profil_views.user_list, name='user_list'),
    path('user/create', profil_views.create_account, name='create_account'),
    path('user/edit/profil', profil_views.edit_profil, name='edit_profil'),
    path('user/<int:pk>/update/account', profil_views.update_account, name='update_account'),



    ##### LIEN APP UOS #####
    path('', uos_views.uo_list, name='uo_list'),
    path('uo/parametres', uos_views.creation_parametre_uo, name='creation_parametre_uo'),
    path('uo/creation', uos_views.create_uo, name='create_uo'),
    path('catalogue/creation', uos_views.create_catalogue_uo, name='create_catalogue_uo'),
    path('uet/creation', uos_views.creation_uet, name='creation_uet'),
    path('plateforme/creation', uos_views.create_plateforme, name='create_plateforme'),
    path('pointage/creation', uos_views.create_pointage, name='create_pointage'),
    path('workpackage/creation', uos_views.create_workpackage, name='create_workpackage'),
    path('perimetre/creation', uos_views.create_perimetre, name='create_perimetre'),
    path('note_cadrage/creation', uos_views.create_note_cadrage, name="create_note_cadrage"),
    path('activite/creation', uos_views.create_activite, name="create_activite"),
    path('pointages', uos_views.pointages, name='pointages'),
    path('historique', uos_views.historique_pointage),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)