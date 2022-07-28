# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.views import direct_etude_view,comptable_ens_view,comptable_view,enseignant_view,administrateur_view,daf_ens_view,daf_view,direct_general_ens_view,direct_general_view,secretaire_ens_view,secretaire_view,direct_etude_ens_view

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    path("direct_etude_ens/",direct_etude_ens_view, name="direct_etude_ens"),
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
    path("secretaire/",secretaire_view, name="secretaire")

]
