"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.contrib.auth.models import User 


class Etablissement(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    code =models.CharField(max_length=100, null=True, blank=True)
    site_web = models.CharField(max_length=50, null=True, blank=True)
    Numero_telephone = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.nom
    
    
class AnneeAcademique(models.Model):
    libelle = models.CharField(max_length=100)
    date_debut = models.DateField(auto_now=False, auto_now_add=False)
    date_fin = models.DateField(auto_now=False,auto_now_add=False)
    
    def __str__(self):
        return self.libelle

        
    
class NiveauScolaire(models.Model):
    choix =(
        
        ('PRIMAIRE', 'Primaire'),
        ('SECONDAIRE', 'Secondaire'),
        ('SUPERIEUR', 'Enseignement supérieur'),
        
    )
    nom = models.CharField(max_length=100,choices=choix)
    etablissement= models.ForeignKey(Etablissement, on_delete=models.SET_NULL, null=True)
    
class Cycle(models.Model):
    nom = models.CharField(max_length=150)
    code =models.CharField(max_length=15,null=True)
    etablissement= models.ForeignKey(Etablissement, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nom
    AnneeAcademique = models.ForeignKey(AnneeAcademique,on_delete=models.SET_NULL,null=True)
   
    
   
   
class Filiere(models.Model):
    nom = models.CharField(max_length=150)
    code =models.CharField(max_length=15,null=True)
    cycle =models.ForeignKey(Cycle, on_delete=models.SET_NULL, null=True)
    AnneeAcademique = models.ForeignKey(AnneeAcademique,on_delete=models.SET_NULL,null=True)
   
    
    def __str__(self):
        return self.nom
    
    
   
    

    
class Classe(models.Model):
    nom = models.CharField(max_length=100)
    code =models.CharField(max_length=15 ,null=True)
    niveau_classe = models.IntegerField(null=True, blank=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True)
    AnneeAcademique = models.ForeignKey(AnneeAcademique,on_delete=models.SET_NULL,null=True)
    frais_scolarite = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    frais_inscription = models.DecimalField(max_digits=10, decimal_places=2, null=True)
   
    def __str__(self):
        return self.nom
    

    
    
    
     

class UnitEnseignement(models.Model):
    nom = models.CharField(max_length=20)
    code =models.CharField(max_length=15,null=True)
    credit = models.SmallIntegerField(null=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)
    
    
    
    

class Matiere(models.Model):
    nom = models.CharField(max_length=10)
    code =models.CharField(max_length=15,null=True)
    unit_ens = models.ForeignKey(UnitEnseignement, on_delete=models.SET_NULL, null=True) 
    coefficient = models.SmallIntegerField(null=True)
    volume_horaire = models.IntegerField(null=True)
   
    def __str__(self):
        return self.nom

    
    
    
    
class Etudiant(models.Model):
    matricule = models.CharField(max_length=15,null=True)
    prenoms = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_naissance = models.DateField(null=True)
   
   
    def __str__(self):
        return self.prenoms + ' ' + self.nom


class Inscription(models.Model):
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE)
    annee_academique = models.ForeignKey('AnneeAcademique', on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inscription de {self.etudiant} en {self.classe} - {self.annee_academique}"

    
        

    
    

