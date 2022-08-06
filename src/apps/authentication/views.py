# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
#from sympy import total_degree 
from .forms import LoginForm, SignUpForm
from apps.authentication.models import Type_user, Intervenant


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            #code permettant d'authentifier l'utilisateur en fonction du speruser
            #si c'est un superuser il regirige vers la page admin de django
            #sinon il le redirige vers le view en question
            user = authenticate(username=username, password=password)
            #ces lignes de code nous permettent de differencier les differentes vues en fonction des roles
            try:
                tout_privillege =Intervenant.objects.filter(username=username).values_list("type_user",flat=True)
                print(tout_privillege)
            except Exception:
                tout_privillege = None
            if user is not None and tout_privillege is not None:
                if len(tout_privillege) < 2:
                    if tout_privillege[0]== 1:
                        login(request, user)
                        #return HttpResponse("c'est la vue Directeur d'etude")
                        return redirect("/directeur_etude/")

                    elif tout_privillege[0]== 2:
                        login(request, user)
                        #return HttpResponse("c'est la vue Secretaire")
                        return redirect("/secretaire/")

                    elif tout_privillege[0]== 3:
                        login(request, user)
                        #return HttpResponse("c'est la vue Directeur général")
                        return redirect("/direct_general/")

                    elif tout_privillege[0]== 4:
                        login(request, user)
                        #return HttpResponse("c'est la vue Enseignant")
                        return redirect("/enseignant/")

                    elif tout_privillege[0]== 5:
                        login(request, user)
                        #return HttpResponse("c'est la vue DAF")
                        return redirect("/daf/")

                    elif tout_privillege[0]== 6:
                        login(request, user)
                        #return HttpResponse("c'est la vue Adminstrateur")
                        return redirect("/admin")

                    elif tout_privillege[0]== 7:
                        login(request, user)
                        #return HttpResponse("c'est la vue Comptable")
                        return redirect("/comptable/")

                else:
                    if 1 in tout_privillege:
                        login(request, user)
                        #return HttpResponse("c'est la vue DE et enseignant")
                        #testons la sortie de la vue avec cette methode de enseignant 
                        #direct_etude_ens_view est une classe qui se retrouve au noveau de home 
                        return redirect("/direct_etude_ens_view")
                    elif 2 in tout_privillege:
                        login(request, user)
                        #return HttpResponse("c'est la vue Secretaire et enseignant")
                        return redirect("/secretaire_ens/")
                    elif 3 in tout_privillege:
                        login(request, user)
                        #return HttpResponse("c'est la vue DG et enseignant")
                        return redirect("/direct_general_ens/")
                    elif 5 in tout_privillege:
                        login(request, user)
                        #return HttpResponse("c'est la vue daf et enseignant")
                        return redirect("/daf_ens/")
                    elif 7 in tout_privillege:
                        login(request, user)
                        #return HttpResponse("c'est la vue Compta et enseignant")
                        return redirect("/comptable_ens/")
            else:
                msg = 'Invalid credentials'

        else:
            msg = 'Error validating the form'

        
            
    
    return render(request, "accounts/login.html", {"form": form, "msg": msg})



def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

