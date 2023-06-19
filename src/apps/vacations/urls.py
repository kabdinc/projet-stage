from django.urls import path
from apps.vacations.views import enseignant_per,enseignant_vac,frais_vacations, gestion_vacations, modifier_taux_horaire, totaux_vacations

urlpatterns = [
    path('gestion_vacations/', gestion_vacations, name='gestion_vacations'),
    path('enseignant_per/', enseignant_per, name='enseignant_per'),
    path('enseignant_vac/', enseignant_vac, name='enseignant_vac'),
    path('frais_vacations/', frais_vacations, name='frais_vacations'),
    path('totaux_vacations/', totaux_vacations, name='totaux_vacations'),
    path('modifier_taux_horaire/<int:enseignant_id>/', modifier_taux_horaire, name='modifier_taux_horaire'),
]