
from django.urls import path
from apps.inscription_frais.views import inscrire_eleve,get_filiere,get_classe,paiement,details_paiement,get_classe_details,get_frais_inscription

urlpatterns = [
   
    path('inscrire_eleve/', inscrire_eleve, name='inscrire_eleve'),
    path('get_filiere/', get_filiere, name='select_filiere'),
    path('select_classe/', get_classe, name='select_classe'),
    path('paiement/', paiement, name='paiement'),
    path('details_paiement/', details_paiement, name='details_paiement'),
    path('get_classe_details/', get_classe_details, name='details_classe'),
    path('get_frais_inscription/', get_frais_inscription, name='get_frais_inscription'),

]