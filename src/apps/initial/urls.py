from django.urls import path
from apps.initial.views import gestion_etudiant, modifier_etudiant, parametrage,create_classe,create_cycle,create_etablissement,create_filiere,create_matiere,create_niveau_scolaire,create_unit_enseignement, supprimer_etudiant,update_classe,update_cycle,update_etablissement,update_filiere,update_matiere,update_niveau_scolaire,update_unit_enseignement,delete_classe,delete_cycle,delete_etablissement,delete_filiere,delete_matiere,delete_niveau_scolaire,delete_unit_enseignement

urlpatterns = [
    
    path("gestion_etudiant/",gestion_etudiant , name="gestion_etudiant"),
    path("creer_niveau/", create_niveau_scolaire, name="creer_niveau"), 
    path("creer_classe/", create_classe, name="creer_classe"), 
    path("creer_filiere/", create_filiere, name="creer_filiere"), 
    path("creer_cycle/", create_cycle, name="creer_cycle"),
    path("creer_classe/", create_classe, name="creer_classe"),
    path("creer_etablissement/", create_etablissement, name="creer_etablissement"), 
    path("creer_ue/", create_unit_enseignement, name="creer_ue"),   
    path("creer_matiere/", create_matiere, name="creer_matiere"),
    path("modifier_niveau/", update_niveau_scolaire, name="modifier_niveau"), 
    path("modifier_classe/", update_classe, name="modifier_classe"), 
    path("modifier_filiere/", update_filiere, name="modifier_filiere"), 
    path("modifier_cycle/<int:cycle_id>/", update_cycle, name="modifier_cycle"),
    path("modifier_etudiant/<int:etudiant_id>/", modifier_etudiant, name="modifier_etudiant,"),
    path("modifier_classe/", update_classe, name="modifier_classe"),
    path("modifier_etablissement/", update_etablissement, name="modifier_etablissement"), 
    path("modifier_ue/", update_unit_enseignement, name="modifier_ue"),   
    path("modifier_matiere/", update_matiere, name="modifier_matiere"),
    path("supprimer_niveau/", delete_niveau_scolaire, name="supprimer_niveau"), 
    path("supprimer_classe/", delete_classe, name="supprimer_classe"), 
    path("supprimer_filiere/", delete_filiere, name="delete_filiere"), 
    path("supprimer_cycle/", delete_cycle, name="supprimer_cycle"),
    path("supprimer_classe/", delete_classe, name="supprimer_classe"),
    path("supprimer_etablissement/", delete_etablissement, name="supprimer_etablissement"), 
    path("supprimer_ue/", delete_unit_enseignement, name="supprimer_ue"),   
    path("supprimer_matiere/", delete_matiere, name="supprimer_matiere"),
    path("supprimer_etudiant/<int:etudiant_id>/", supprimer_etudiant, name="supprimer_etudiant,"),
    path("parametrage/", parametrage, name="parametrage"), 
  
]   




