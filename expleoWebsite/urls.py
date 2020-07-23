
from django.contrib import admin
from django.conf.urls import url
from .import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diagramme', views.diagramme),
    
    ##### LIEN APP UOS #####
    path('', include('uos.urls')),
    ##### LIEN APP PROFIL #####
    path('account/', include('profil.urls')),
    ##### LIEN APP AUTOMATIC #####
    path('automatic/', include('automatic.urls')),
    ##### LIEN APP SEND EMAIL #####
    path('email/', include('send_mail.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
