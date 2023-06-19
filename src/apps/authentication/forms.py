# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.authentication.models import  Intervenant, Type_user
from apps.maquette.models import Classe, Matiere

"""vu que nous utilisons intervenant comme reference de user par defaut il faudrait spécifier
dans le form que nos utiliserons notre propre model d'ou l'importation de cette fonction 
"""
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from apps.authentication.models import Intervenant 
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "nom d'utilisateur",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "mot de passe",
                "class": "form-control"
            }
        ))




class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))
    type_user = forms.ModelMultipleChoiceField(
        queryset=Type_user.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input"
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = Intervenant
        fields = ('username', 'email', 'password1', 'password2', 'type_user')


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from .models import Intervenant, Type_user

class EnseignantForm(UserCreationForm):
    STATUT_CHOICES = [
        ('permanent', 'Permanent'),
        ('vacataire', 'Vacataire'),
    ]

    type_user = forms.ModelChoiceField(
        queryset=Type_user.objects.filter(name='ENSEIGNANT'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    statut = forms.ChoiceField(
        choices=STATUT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        self.fields['password2'] = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = Intervenant
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'type_user', 'statut')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user.type_user.add(self.cleaned_data['type_user'])
        return user

from django import forms
from .models import Intervenant

class AllouerMatiereForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Prénom",
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )
    last_name = forms.CharField(
        label="Nom",
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )
    matieres = forms.ModelMultipleChoiceField(
        queryset=Matiere.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
   
    class Meta:
        model = Intervenant
        fields = ('first_name', 'last_name', 'matieres')
        
    def save(self, enseignant):
        matieres = self.cleaned_data.get('matieres')
        enseignant.matieres.set(matieres)
        enseignant.save()

