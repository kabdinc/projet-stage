# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from pyexpat import model
from typing import Any, Optional
from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models 
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from apps.maquette.models import Classe, Matiere

# Create your models here.


class Type_user(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Type_detail", kwargs={"pk": self.pk})


# create de la classe intervenant qui hérite de la classe user


class Intervenant(AbstractUser):
    
    STATUT_CHOICES = [
        ('permanent', 'Permanent'),
        ('vacataire', 'Vacataire'),
    ]
     
   
     
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, null=True, blank=True)    
    type_user = models.ManyToManyField(Type_user)
    taux_horaire = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    matieres = models.ManyToManyField(Matiere)
    objects = UserManager()


