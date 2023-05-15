from django.urls import path
from apps.initial.views import parametrage

urlpatterns = [
   
   
    path("parametrage/", parametrage, name="parametrage"), 
  
]   




