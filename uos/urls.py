from . import views
from django.urls import path
from uos import views as uos_views
from uos.views import ActivitessList

urlpatterns = [

    ##### LIEN APP UOS #####
    path('', uos_views.uo_list, name='uo_list'),
    path('uos/list', uos_views.uo_list, name='uoslist'),
    path('uo/parametres', uos_views.creation_parametre_uo, name='creation_parametre_uo'),
    path('uo/creation', uos_views.create_uo, name='create_uo'),
    path('administration', uos_views.administration, name='administration'),
    path('catalogue/creation', uos_views.create_catalogue_uo, name='create_catalogue_uo'),
    path('uet/creation', uos_views.creation_uet, name='creation_uet'),
    path('plateforme/creation', uos_views.create_plateforme, name='create_plateforme'),
    path('pointage/creation', uos_views.create_pointage, name='create_pointage'),
    path('workpackage/creation', uos_views.create_workpackage, name='create_workpackage'),
    path('perimetre/creation', uos_views.create_perimetre, name='create_perimetre'),
    path('avancement/creation', uos_views.create_avancement, name='create_avancement'),
    path('note_cadrage/creation', uos_views.create_note_cadrage, name="create_note_cadrage"),
    path('activite/creation', uos_views.create_activite, name="create_activite"),
    path('pointages', uos_views.pointages, name='pointages'),
    path('historique', uos_views.historique_pointage),
    path('uo/<int:pk>/update', uos_views.update_uos, name='update_uos'),

    path('statistique', uos_views.uo_statistique, name='uo_statistique'),

    path('act/',uos_views.ActivitessList,name='activitelist'),
    path('projetlist/',uos_views.projet_list,name='projet_list'),
    path('fonctionlist/',uos_views.fonction_list,name='fonction_list'),
    path('plateformelist/',uos_views.plateforme_list,name='plateforme_list'),
    path('uetlist/',uos_views.uet_list,name='uet_list'),
    path('cadrage/',uos_views.cadrage_list,name='cadrage_list'),


    # Import export Excel
    path('uo/export', uos_views.excel_generator, name='excel_generator'),
    path('import/', uos_views.excel_import, name='excel_import'),
    path('import/uo/<int:pk>/', uos_views.excel_import_data , name='import_data_uo'),   
]
