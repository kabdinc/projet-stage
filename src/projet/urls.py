"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.home.views import direct_etude_ens_view,direct_etude_view,comptable_ens_view,comptable_view,enseignant_view,administrateur_view,daf_ens_view,daf_view,direct_general_ens_view,direct_general_view,secretaire_ens_view,secretaire_view,double_role
from apps.inscription_frais.views import details_paiement, etat_paiement, gestion_inscription_frais, inscrire_eleve,inscrire_eleve,get_classe,get_filiere, liste_classes, liste_etudiant, modifier_frais,paiement,get_classe_details,get_frais_inscription,recu_inscription, reinscrire_eleve, selection_eleve
from apps.initial.views import associer_matiere, creer_annee, delete_enseignant, gestion_annee, gestion_etudiant, modifier_annee, modifier_enseignant, modifier_etudiant, parametrage,create_classe,create_cycle,create_etablissement,create_filiere,create_matiere,create_niveau_scolaire,create_unit_enseignement, supprimer_etudiant,update_classe,update_cycle,update_etablissement,update_filiere,update_matiere,update_niveau_scolaire,update_unit_enseignement,delete_classe,delete_cycle,delete_etablissement,delete_filiere,delete_matiere,delete_niveau_scolaire,delete_unit_enseignement,gestion_etablissement,gestion_cycle,gestion_filiere,gestion_classe,liste_etablissements,gestion_ue,gestion_matiere,gestion_enseignant,creer_enseignant
from apps.vacations.views import enseignant_per, enseignant_vac, frais_vacations, gestion_vacations, modifier_taux_horaire, totaux_vacations

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE

    #dans le urls.py de mon projet meme je vient creer mes liens en foncti de mes vues
    path("direct_etude_ens_view", direct_etude_ens_view, name="vue_de_ens" ),
    path("directeur_etude/", direct_etude_view, name="directeur_etude"),
    path("comptable_ens/", comptable_ens_view, name="comptable_ens"),
    path("comptable/", comptable_view, name="comptable"), 
    path("enseignant/", enseignant_view, name="enseignant"), 
    path("administrateur/", administrateur_view, name="administrateur"), 
    path("daf_ens/", daf_ens_view, name="daf_ens"),
    path("daf/",daf_view, name="daf"),
    path("direct_general_ens/",direct_general_ens_view, name="direct_general_ens"), 
    path("direct_general/",direct_general_view, name="direct_general"),
    path("secretaire_ens/",secretaire_ens_view, name="secretaire_ens"),
    path("secretaire/",secretaire_view, name="secretaire"),
    path("double_role",double_role ,name="double_role"),
    path("inscrire_eleve/",inscrire_eleve,name="inscrire_eleve"),
    path("reinscrire_eleve/<int:etudiant_id>/",reinscrire_eleve,name="reinscrire_eleve"),
    path('get_filiere/', get_filiere, name='get_filiere'),
    path('get_classe/', get_classe, name='get_classe'),
    path('paiement/', paiement, name='paiement'),
    path('get_frais_inscription/', get_frais_inscription, name='get_frais_inscription'),
    path("apps.inscription_frais/",include("apps.inscription_frais.urls")),
    path('get_classe_details/', get_classe_details, name='details_classe'),
    path('recu_inscription/<int:inscription_id>/', recu_inscription, name='recu_inscription'),
    path('selection_eleve/', selection_eleve, name='selection_eleve'),
  
    path("parametrage/", parametrage, name="parametrage"), 
    path("creer_niveau/", create_niveau_scolaire, name="creer_niveau"), 
    path("creer_classe/", create_classe, name="creer_classe"), 
    path("creer_filiere/", create_filiere, name="creer_filiere"), 
    path("creer_cycle/", create_cycle, name="creer_cycle"),
    path("creer_classe/", create_classe, name="creer_classe"),
    path("creer_etablissement/", create_etablissement, name="creer_etablissement"), 
    path("creer_ue/", create_unit_enseignement, name="creer_ue"),   
    path("creer_matiere/", create_matiere, name="creer_matiere"),
    path("creer_enseignant/", creer_enseignant, name="creer_enseignant"),
    path("modifier_niveau/", update_niveau_scolaire, name="modifier_niveau"), 
    path("modifier_classe/", update_classe, name="modifier_classe"), 
    path("modifier_filiere/<int:filiere_id>/", update_filiere, name="modifier_filiere"), 
    path("modifier_cycle/<int:cycle_id>/", update_cycle, name="modifier_cycle"),
    path("modifier_classe/<int:classe_id>/", update_classe, name="modifier_classe"),
    path("modifier_etablissement/<int:etablissement_id>/", update_etablissement, name="modifier_etablissement"), 
    path("modifier_ue/<int:unitenseignement_id>/", update_unit_enseignement, name="modifier_ue"),   
    path("modifier_matiere/<int:matiere_id>/", update_matiere, name="modifier_matiere"),
    path("modifier_enseignant/<int:enseignant_id>/", modifier_enseignant, name="modifier_enseignant"),
    path("modifier_etudiant/<int:etudiant_id>/", modifier_etudiant, name="modifier_etudiant"),
    path("supprimer_etudiant/<int:etudiant_id>/", supprimer_etudiant, name="supprimer_etudiant"),
    path("supprimer_niveau/", delete_niveau_scolaire, name="supprimer_niveau"), 
    path("supprimer_classe/<int:classe_id>/", delete_classe, name="supprimer_classe"), 
    path("supprimer_filiere/<int:filiere_id>/", delete_filiere, name="delete_filiere"), 
    path("supprimer_cycle/<int:cycle_id>/", delete_cycle, name="supprimer_cycle"),
    path("supprimer_etablissement/<int:etablissement_id>/", delete_etablissement, name="supprimer_etablissement"), 
    path("supprimer_ue/<int:unitenseignement_id>/", delete_unit_enseignement, name="supprimer_ue"),   
    path("supprimer_matiere/<int:matiere_id>/", delete_matiere, name="supprimer_matiere"),
    path("supprimer_enseignant/<int:enseignant_id>/", delete_enseignant, name="supprimer_enseignant"),
    path("gestion_etablissement/", gestion_etablissement, name="gestion_etablissement"),
    path("gestion_cycle/", gestion_cycle, name="gestion_cycle"),
    path("gestion_filiere/", gestion_filiere, name="gestion_filiere"),
    path("gestion_classe/", gestion_classe, name="gestion_classe"),
    path("liste_etablissements/", liste_etablissements, name="liste_etablissements"),
    path("gestion_ue/", gestion_ue, name="gestion_ue"),
    path("gestion_matiere/", gestion_matiere, name="gestion_matiere"),
    path("gestion_enseignant/", gestion_enseignant, name="gestion_enseignant"),
    path("associer_matiere/<int:enseignant_id>/", associer_matiere, name="associer_matiere"),
    path("gestion_etudiant/",gestion_etudiant , name="gestion_etudiant"),
    
    path('gestion_vacations/', gestion_vacations, name='gestion_vacations'),
    path('enseignant_vac/', enseignant_vac, name='enseignant_vac'),
    path('enseignant_per/', enseignant_per, name='enseignant_per'),
    path('frais_vacations/<int:enseignant_id>', frais_vacations, name='frais_vacations'),
    path('totaux_vacations/', totaux_vacations, name='totaux_vacations'),
    path('modifier_taux_horaire/<int:enseignant_id>/', modifier_taux_horaire, name='modifier_taux_horaire'),
    path('liste_etudiant/', liste_etudiant, name='liste_etudiant'),
    path('etat_paiement/<int:etudiant_id>', etat_paiement, name='etat_paiement'),
    path('details_paiement/<int:paiement_id>/<int:etudiant_id>/<int:classe_id>', details_paiement, name='details_paiement'),
    path('modifier_frais/<int:classe_id>', modifier_frais, name='modifier_frais'),
    path('liste_classes/', liste_classes, name='liste_classes'),
    path('gestion_inscription_frais/', gestion_inscription_frais, name='gestion_inscription_frais'),
    path("gestion_annee/",gestion_annee , name="gestion_annee"),
    path("creer_annee/",creer_annee  , name="creer_annee"),
    path("modifier_annee/<int:AnneeAcademique_id>", modifier_annee, name="modifier_annee"), 
   




    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
    path("",include("apps.inscription_frais.urls") ),
    path("",include("apps.initial.urls") ),
    path("",include("apps.vacations.urls") ),
   
]
