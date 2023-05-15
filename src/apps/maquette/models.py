"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.contrib.auth.models import User

class Etablissement(models.Model):
    nom = models.CharField(max_length=100)
    
class AnneeAcademique(models.Model):
    libelle = models.CharField(max_length=100)
    date_debut = models.DateField(auto_now=False, auto_now_add=False)
    date_fin = models.DateField(auto_now=False,auto_now_add=False)
    
    def __str__(self):
        return self.libelle

        
    
class NiveauScolaire(models.Model):
    nom = models.CharField(max_length=100)
    etablissement= models.ForeignKey(Etablissement, on_delete=models.SET_NULL, null=True)
    
class Cycle(models.Model):
    nom = models.CharField(max_length=100)
    code =models.CharField(max_length=15,null=True)
    etablissement= models.ForeignKey(Etablissement, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nom
    AnneeAcademique = models.ForeignKey(AnneeAcademique,on_delete=models.SET_NULL,null=True)
   
    
   
   
class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    code =models.CharField(max_length=15,null=True)
    cycle =models.ForeignKey(Cycle, on_delete=models.SET_NULL, null=True)
    AnneeAcademique = models.ForeignKey(AnneeAcademique,on_delete=models.SET_NULL,null=True)
   
    
    def __str__(self):
        return self.nom
    
    
   
    

    
class Classe(models.Model):
    nom = models.CharField(max_length=5)
    code =models.CharField(max_length=15 ,null=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True)
    AnneeAcademique = models.ForeignKey(AnneeAcademique,on_delete=models.SET_NULL,null=True)
   
    def __str__(self):
        return self.nom
    

    
    
    
     

class UnitEnseignement(models.Model):
    nom = models.CharField(max_length=20)
    code =models.CharField(max_length=15,null=True)
    credit = models.SmallIntegerField(null=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)
    
    
    
    

class Matiere(models.Model):
    nom = models.CharField(max_length=10)
    unit_ens = models.ForeignKey(UnitEnseignement, on_delete=models.SET_NULL, null=True) 
    coefficient = models.SmallIntegerField(null=True)
    
    
class Etudiant(models.Model):
    prenoms = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_naissance = models.DateField(null=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)
    AnneeAcademique = models.ForeignKey(AnneeAcademique,on_delete=models.SET_NULL,null=True)
   
    def __str__(self):
        return self.prenoms + ' ' + self.nom



    
        

    
    

