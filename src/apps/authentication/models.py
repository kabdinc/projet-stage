# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.
class Intervenant(models.Model):
    nom_inter = models.CharField(max_length=50)
    prenoms_inter = models.CharField(max_length=150)
    nom_utilisateur = models.CharField(max_length=50,blank=False)
    mot_de_passe = models.CharField(max_length=200,blank=False)
