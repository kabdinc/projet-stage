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
from apps.inscription_frais.views import inscrire_eleve,inscrire_eleve,get_classe,get_filiere,paiement,details_paiement,get_classe_details,get_frais_inscription
from apps.initial.views import parametrage,create_classe,create_cycle,create_etablissement,create_filiere,create_matiere,create_niveau_scolaire,create_unit_enseignement,update_classe,update_cycle,update_etablissement,update_filiere,update_matiere,update_niveau_scolaire,update_unit_enseignement,delete_classe,delete_cycle,delete_etablissement,delete_filiere,delete_matiere,delete_niveau_scolaire,delete_unit_enseignement,gestion_etablissement,gestion_cycle

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
    path('get_filiere/', get_filiere, name='get_filiere'),
    path('get_classe/', get_classe, name='get_classe'),
    path('paiement/', paiement, name='paiement'),
    path('get_frais_inscription/', get_frais_inscription, name='get_frais_inscription'),
    path('details_paiement/', details_paiement, name='details_paiement'),
    path("apps.inscription_frais/",include("apps.inscription_frais.urls")),
    path('get_classe_details/', get_classe_details, name='details_classe'),
  
    path("parametrage/", parametrage, name="parametrage"), 
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
    path("'modifier_cycle/<int:cycle_id>/'/", update_cycle, name="modifier_cycle"),
    path("modifier_classe/", update_classe, name="modifier_classe"),
    path("modifier_etablissement/", update_etablissement, name="modifier_etablissement"), 
    path("modifier_ue/", update_unit_enseignement, name="modifier_ue"),   
    path("modifier_matiere/", update_matiere, name="modifier_matiere"),
    path("supprimer_niveau/", delete_niveau_scolaire, name="supprimer_niveau"), 
    path("supprimer_classe/", delete_classe, name="supprimer_classe"), 
    path("supprimer_filiere/", delete_filiere, name="delete_filiere"), 
    path("supprimer_cycle/<int:cycle_id>/", delete_cycle, name="supprimer_cycle"),
    path("supprimer_classe/", delete_classe, name="supprimer_classe"),
    path("supprimer_etablissement/", delete_etablissement, name="supprimer_etablissement"), 
    path("supprimer_ue/", delete_unit_enseignement, name="supprimer_ue"),   
    path("supprimer_matiere/", delete_matiere, name="supprimer_matiere"),
    path("gestion_etablissement/", gestion_etablissement, name="gestion_etablissement"),
     path("gestion_cycle/", gestion_cycle, name="gestion_cycle"),


    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
    path("",include("apps.inscription_frais.urls") ),
    path("",include("apps.initial.urls") ),
   
]
