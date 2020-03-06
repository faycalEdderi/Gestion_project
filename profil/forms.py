
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.forms import ModelForm


# FORM DE CREATION DE COMPTE
# Uniquement pour RT et +
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )
    username = forms.CharField(
        required=False,
    )
    first_name = forms.CharField(
        label='Prénom : ',
        required=True,
        error_messages={'required': 'Veuillez entrer un prénom'},

    )
    last_name = forms.CharField(
        label='Nom : ',
        required=True,
        error_messages={'required': 'Veuillez entrer un nom'},

    )
    password1 = forms.CharField(
        label="Mot de passe",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label="Saisir à nouveau le mot de passe",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):

    phone_number = forms.CharField(
        label='Téléphone : ',
        required=False,
        error_messages={'required': 'Problème avec le numéro de téléphone'},

    )

    role = forms.ModelChoiceField(
        label="Selectionner un role :",
        queryset=Role.objects.all()

    )

    poste = forms.ModelChoiceField(
        label = "Selectionner un poste :",
        queryset=NewPostName.objects.all(),
        required= False,
    )

    class Meta : 
        model = MyUsers
        fields = (
            'phone_number',
            'poste',
            'role',

        )


class CreateExecutant(forms.ModelForm):
    pilote = forms.ModelChoiceField(
        required=False,
        queryset=Pilote.objects.all(),
        label= "Pilote responsable"
    )

    class Meta :
        model = Executant
        fields =(
            'superior',
        )


class AjoutPosteForm(forms.ModelForm):
    post_name = forms.CharField(required=False)

    class Meta:
        model = NewPostName
        fields =(
            'post_name',
        )

        error_messages = {
            'post_name': {
                'unique': 'Ce poste existe déja !'
            },
        }


# Edit Profil pour user connecté
class EditProfileForm(forms.ModelForm):

    image = forms.ImageField(
        required=False,
        error_messages={ 'invalid': "Veuillez selectionner uniquement un fichier de type "
                                    "image"},
        widget=forms.FileInput,
    )
    phone_number = forms.CharField(
        required=False,
        label="Téléphone",
        error_messages={
            'invalid': "Veuillez entrer un numéro de téléphone valide"}
    )

    class Meta:
        model = MyUsers
        fields = (
            'phone_number',
            'image',
        )


# Formulaire permettant a un superieur de modifier les comptes
class EditAccountForm(forms.ModelForm):


    phone_number = forms.CharField(
        required=False,
        label="Téléphone",
        error_messages={
            'invalid': "Veuillez entrer un numéro de téléphone valide"}
    )
    email = forms.EmailField(
        label='Email :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )

    first_name = forms.CharField(
        label='Prénom : ',
        required=True,
        error_messages={'required': 'Veuillez entrer un prénom'},

    )
    last_name = forms.CharField(
        label='Nom : ',
        required=True,
        error_messages={'required': 'Veuillez entrer un nom'},

    )
    role = forms.ModelChoiceField(
        label="Selectionner un role :",
        queryset=Role.objects.all()

    )

    poste = forms.ModelChoiceField(
        label="Selectionner un poste :",
        queryset=NewPostName.objects.all(),
        required=False,
    )

    class Meta:
        model = MyUsers
        fields = (
            'phone_number',
            'first_name',
            'last_name',
            'email',
            'role',
            'poste'
        )