
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import * 
from django.forms import ModelForm


# FORM DE CREATION DE COMPTE 
#Uniquement pour RT et +
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},
        )
    username = forms.CharField(
        required=False,
        )
    first_name = forms.CharField(
        required=True,
        error_messages={'required': 'Veuillez entrer un Nom'},
         
        )
    last_name = forms.CharField(
        required=True,
        error_messages={'required': 'Veuillez entrer un Prénom'},
        
        )
    password1 = forms.CharField(
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'}, 
        widget=forms.PasswordInput, 
      
        )
    password2 = forms.CharField(
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
    poste = forms.ModelChoiceField(
        label = "Seectionner un poste :",
        queryset=NewPostName.objects.all()
    )
    class Meta : 
        model = UserProfile 
        fields = (
            'poste',
            'image', 
            'role'    
        )

       
class LivForm(forms.ModelForm):   
    class Meta : 
        model = Liv
        fields = (
           'executant', 
           'rt_liv',            
        )


class ChValidForm(forms.ModelForm):
    chValid_list=forms.CharField(
        required=False,
    )

    class Meta:
        model = ChValid
        fields =(
            'responsable',    
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


# FORM MODIFICATION DE PROFIL ACCESSIBLE PAR TOUS USER

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        error_messages={'required': 'Veuillez entrer un prénom'}, 
         
        )
    # ajout de class bootstrap pour modifier le style de l'input
    first_name.widget = forms.TextInput(attrs={'class': 'form-control',})
    
    last_name = forms.CharField(
        required=True,
        error_messages={'required': 'Veuillez entrer un nom'},
        )
    last_name.widget = forms.TextInput(attrs={'class': 'form-control',})

    image = forms.ImageField(
        required=False, 
        widget=forms.FileInput,  
         
        )
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},
        ) 
    email.widget = forms.TextInput(attrs={'readonly': '',})

    class Meta:
        model = User
        
        fields = (     
            'first_name',
            'last_name',
            'email', 
        )


class EditProfileUserForm(ModelForm):
    POSTE = (
        ('ch.MIL', 'CH.MIL'),
        ('ch.HIL', 'CH.HIL '), 
        ('ch.IS', 'CH.IS '),
        ('liv', 'LIV'),
        ('rt', 'RT '),
        ('pmo', 'PMO'),
        ('rsop', 'RSOP'),
        
    ) 

    poste = forms.ChoiceField(choices=POSTE, widget=forms.Select(attrs={'class': 'custom-select mr-sm-2"'}) )

    image = forms.ImageField(
        required=False,
        error_messages = {'invalid': "Veuillez selectionner uniquement un fichier de type image" },
        widget=forms.FileInput,  
        )
  
    class Meta:
        model = UserProfile
        fields = ( 
            'image', 
            'poste',
            'is_active',
        )