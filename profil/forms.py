from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
from django.forms import ModelForm
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView, 
    UpdateView
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
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
    class Meta : 
        model = UserProfile
        fields = (
            'poste',
            'image'
            
        )


class EditProfileForm(forms.ModelForm, UpdateView):

    class Meta:
        model = User
        
        fields = ( 
            
            'first_name',
            'last_name', 
        )
class EditProfileUserForm(ModelForm):

    class Meta:
        model = UserProfile
        
        fields = ( 
            
            'image', 
            'role',
        )





    



