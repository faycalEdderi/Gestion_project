from django.conf.urls import url
from send_mail import views
from django.urls import path

urlpatterns = [
    path('send_email/rappel/pointage', views.reminder_pointage, name="pointage_reminder")
]
