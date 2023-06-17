from apps.authentication.models import Intervenant
from django.db import models

class TypeEnseignant(models.Model):
    TYPE_CHOICES = (
        ('permanent', 'Enseignant Permanent'),
        ('vacataire', 'Enseignant Vacataire'),
    )
    intervenant = models.OneToOneField(Intervenant, on_delete=models.CASCADE)
    type_enseignant = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.intervenant.username} - {self.get_type_enseignant_display()}"