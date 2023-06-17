# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from pyexpat import model
from typing import Any, Optional
from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models 
from django.urls import reverse

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
   type_user = models.ManyToManyField(Type_user)
   
  
  
class Manager(UserManager):
    def create_user(self, username, password=None):
        user = self.model()
        user.set_password(password)
        user.save()
        return user
    
    

