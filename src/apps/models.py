from django.db import models

# Create your models here.
class Intervenant(models.Model):
    nom_inter = models.CharField(max_length=50,blank=False)
    prenoms = models.CharField(max_length=150,blank=False)
    nom_utilisateur = models.CharField(max_length=20,blank=False)
    mot_de_passe = models.CharField(max_length=30,blank=False)