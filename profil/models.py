from django import forms
from django.db import models
from django.contrib.auth.models import User
import random


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    filebase = ''.join((random.choice(chars)) for x in range(20))

    return "%s/%s.%s" % (instance.id, filebase, extension)


class NewPostName(models.Model):
    post_name = models.CharField(
        max_length=150,
        unique=True,
        error_messages={'unique': "Ce poste existe déja !"},
    )

    def __str__(self):
        return self.post_name


class Role(models.Model):
    role_name = models.CharField(
        max_length=150,
        unique=True
    )

    def __str__(self):
        return self.role_name


class MyUsers(User):

    phone_number =  models.CharField(
        max_length=100)

    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)

    poste = models.ForeignKey(
        NewPostName,
        null=True,
        blank=True,

        on_delete=models.PROTECT,
    )

    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.last_name  + " " +  self.first_name

    class Meta:
        verbose_name = 'MyUser'


class Client(models.Model):
    responsableUET = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    email = models.EmailField(max_length=50)

    phone_number = models.PositiveIntegerField(
        blank=True,
        max_length=10
    )

    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Client'


# un user chef hérite de mes user et il peut avoir un responsable qui a un profil chef comme
# lui
class RespSOP(MyUsers):
    responsable = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'SOP / Responsable d\'activitée'


# un user chef de projet hérite de mes user et il peut avoir un responsable chef
class ChefdeProjet(MyUsers):
    superior = models.ForeignKey(RespSOP,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Chef de projet'


class RespTechnique(MyUsers):
    superior = models.ForeignKey(ChefdeProjet,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'RT'


class Pilote(MyUsers):
    superior = models.ForeignKey(RespTechnique,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Pilote d\'activité'


class Executant(MyUsers):
    superior = models.ForeignKey(Pilote,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Executant'









