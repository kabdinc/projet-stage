
from django.urls import path
from apps.inscription_frais.views import inscrire_eleve,get_filiere,get_classe

urlpatterns = [
   
    path('inscrire_eleve/', inscrire_eleve, name='inscrire_eleve'),
    path('get_filiere/', get_filiere, name='select_filiere'),
    path('select_classe/', get_classe, name='select_classe'),
]