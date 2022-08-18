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
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]
