from django.db import models
from apps.maquette.models import Cycle, Filiere, Classe,Etudiant,AnneeAcademique



class RecuInscription(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    frais_inscription = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reçu d'inscription pour {self.eleve} - {self.date}"

    
    
    
class Paiement(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)


    
  
    