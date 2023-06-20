
from django.urls import path
from apps.inscription_frais.views import etat_paiement, inscrire_eleve,get_filiere,get_classe,paiement,get_classe_details,get_frais_inscription,recu_inscription,liste_etudiant,liste_classes,modifier_frais,gestion_inscription_frais,details_paiement

urlpatterns = [
    path('modifier_frais/<int:classe_id>', modifier_frais, name='modifier_frais'),
    path('etat_paiement/<int:etudiant_id>', etat_paiement, name='etat_paiement'),
    path('details_paiement/<int:paiement_id>/<int:etudiant_id>/<int:classe_id>', details_paiement, name='details_paiement'),
    path('inscrire_eleve/', inscrire_eleve, name='inscrire_eleve'),
    path('get_filiere/', get_filiere, name='select_filiere'),
    path('select_classe/', get_classe, name='select_classe'),
    path('paiement/', paiement, name='paiement'),
    path('get_classe_details/', get_classe_details, name='details_classe'),
    path('get_frais_inscription/', get_frais_inscription, name='get_frais_inscription'),
    path('recu_inscription/<int:inscription_id>/', recu_inscription, name='recu_inscription'),
    path('liste_etudiant/', liste_etudiant, name='liste_etudiant'),
    path('liste_classes/', liste_classes, name='list_classes'),
    path('gestion_inscription_frais/', gestion_inscription_frais, name='gestion_inscription_frais'),
    

]