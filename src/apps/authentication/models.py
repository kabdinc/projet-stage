# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# create de la classe intervenant qui hérite de la classe user
class Intervenant(AbstractUser):
    Type = models.CharField(blank=False,max_length=50)
  