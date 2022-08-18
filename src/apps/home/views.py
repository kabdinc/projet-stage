# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from apps.authentication.views import login_view


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def direct_etude_view(request):
     html_templat = loader.get_template('accounts/register.html')
     return render(request,html_templat,context={})

#sur la classe qui va sortir chaque page html on devra mettre un login required et ensuite specifier la page a creer dans le render
#pur le context on pourra ajouter les variable qu'on voudra exporter apres 
@login_required(login_url="/login/")
def direct_etude_ens_view(request):
     html_template = loader.get_template('home/index.html')
     return render(request,"home/de.html")

@login_required(login_url="/login/")  
def secretaire_view(request):

     html_template = loader.get_template('home/secretaire.html')
     return render(request,"home/secretaire.html",context={})

@login_required(login_url="/login/")  
def secretaire_ens_view(request):
      html_template = loader.get_template('home/index.html')
      return render(request,"home/index.html",context={}) 
 
@login_required(login_url="/login/")  
def direct_general_view(request):
      html_template = loader.get_template('home/index.html')
      return render(request,"home/index.html",context={})

@login_required(login_url="/login/")
def direct_general_ens_view(request):
     html_template = loader.get_template('home/index.html')
     return render(request,"home/index.html",context={}) 

@login_required(login_url="/login/")  
def daf_view(request):
     html_template = loader.get_template('home/index.html')
     return render(request,"home/index.html",context={})

@login_required(login_url="/login/")  
def daf_ens_view(request):
     html_template = loader.get_template('home/index.html')
     return render(request,"home/index.html",context={})

@login_required(login_url="/login/")  
def administrateur_view(request):
     html_template = loader.get_template('home/index.html')
     return render(request,"home/index.html",context={})

@login_required(login_url="/login/")  
def enseignant_view(request):
     html_template = loader.get_template('home/index.html')
     return render(request,"home/index.html",context={})  

@login_required(login_url="/login/")  
def comptable_view(request):
      html_template = loader.get_template('home/index.html')
      return render(request,"home/index.html",context={}) 

@login_required(login_url="/login/")  
def comptable_ens_view(request):
      html_template = loader.get_template('home/index.html')
      return render(request,"home/index.html",context={}) 
