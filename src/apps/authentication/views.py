# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from sympy import total_degree 
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
                        return HttpResponse("c'est la vue Directeur d'etude")
                        #return redirect("/admin")

                    elif tout_privillege[0]== 2:
                        login(request, user)
                        return HttpResponse("c'est la vue Secretaire")
                        #return redirect("/admin")

                    elif tout_privillege[0]== 3:
                        login(request, user)
                        return HttpResponse("c'est la vue Directeur général")
                        #return redirect("/admin")

                    elif tout_privillege[0]== 4:
                        login(request, user)
                        return HttpResponse("c'est la vue Enseignant")
                        #return redirect("/admin")

                    elif tout_privillege[0]== 5:
                        login(request, user)
                        return HttpResponse("c'est la vue DAF")
                        #return redirect("/admin")

                    elif tout_privillege[0]== 6:
                        login(request, user)
                        return HttpResponse("c'est la vue Adminstrateur")
                        #return redirect("/admin")

                    elif tout_privillege[0]== 7:
                        login(request, user)
                        return HttpResponse("c'est la vue Comptable")
                        #return redirect("/admin")

                else:
                    if 1 in tout_privillege:
                        login(request, user)
                        return HttpResponse("c'est la vue DE et enseignant")
                        #return redirect("/admin")
                    elif 2 in tout_privillege:
                        login(request, user)
                        return HttpResponse("c'est la vue Secretaire et enseignant")
                        #return redirect("/admin")
                    elif 3 in tout_privillege:
                        login(request, user)
                        return HttpResponse("c'est la vue DG et enseignant")
                        #return redirect("/admin")
                    elif 5 in tout_privillege:
                        login(request, user)
                        return HttpResponse("c'est la vue daf et enseignant")
                        #return redirect("/admin")
                    elif 7 in tout_privillege:
                        login(request, user)
                        return HttpResponse("c'est la vue Compta et enseignant")
                        #return redirect("/admin")
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
