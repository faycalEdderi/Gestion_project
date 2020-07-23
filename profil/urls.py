from . import views
from django.urls import path
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from profil import views as profil_views


urlpatterns = [

    path('connexion', profil_views.connexion, name='connexion'),
    path('profil', profil_views.display_profil, name="profil"),
    path('change/mdp', profil_views.change_pwd, name='modifMdp'),
    path('users/list', profil_views.user_list, name='user_list'),
    path('user/create', profil_views.create_account, name='create_account'),
    path('user/edit/profil', profil_views.edit_profil, name='edit_profil'),
    path('user/<int:pk>/update/account', profil_views.update_account, name='update_account'),

    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset_password", PasswordResetView.as_view(), name='reset_password'),
    path("reset_password/done", PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
