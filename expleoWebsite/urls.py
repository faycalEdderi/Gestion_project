
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.uo),
    path('profil', views.profil, name="profil"),
    path('diagramme', views.diagramme),
    path('pointages', views.pointages, name='pointages'),
    path('uo', views.uo, name="uo"),
    path('historique', views.historique),
    path('connexion', views.connexion, name='connexion'),

    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset_password", PasswordResetView.as_view(), name='reset_password'),
    path("reset_password/done", PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register', profil_views.register, name='register'),
    path('edit_profile', profil_views.edit_profile, name='edit_profile'),
    path('modifMdp', profil_views.change_pwd, name='modifMdp'),
    path('userList', profil_views.user_list, name='user_list'),
    
    path('user/<int:id>/update/', profil_views.update_user, name='update_user'),
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



