
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from apps.maquette.models import Etablissement, AnneeAcademique, NiveauScolaire, Cycle, Filiere, Classe, UnitEnseignement, Matiere
from .forms import EtablissementForm, AnneeAcademiqueForm, NiveauScolaireForm, CycleForm, FiliereForm, ClasseForm, UnitEnseignementForm, MatiereForm

def parametrage(request):
    etablissement_form = EtablissementForm()
    annee_academique_form = AnneeAcademiqueForm()
    niveau_scolaire_form = NiveauScolaireForm()
    cycle_form = CycleForm()
    filiere_form = FiliereForm()
    classe_form = ClasseForm()
    ue_form = UnitEnseignementForm()
    matiere_form = MatiereForm()
    context = {'etablissement_form': etablissement_form, 
               'annee_academique_form': annee_academique_form,
               'niveau_scolaire_form': niveau_scolaire_form,
               'cycle_form': cycle_form,
               'filiere_form': filiere_form,
               'classe_form': classe_form,
               'ue_form': ue_form,
               'matiere_form': matiere_form}
    if request.method == 'POST':
        if 'etablissement-form' in request.POST:
            etablissement_form = EtablissementForm(request.POST)
            if etablissement_form.is_valid():
                etablissement_form.save()
                return redirect('parametrage')
        elif 'annee-academique-form' in request.POST:
            annee_academique_form = AnneeAcademiqueForm(request.POST)
            if annee_academique_form.is_valid():
                annee_academique_form.save()
                return redirect('parametrage')
        elif 'niveau-scolaire-form' in request.POST:
            niveau_scolaire_form = NiveauScolaireForm(request.POST)
            if niveau_scolaire_form.is_valid():
                niveau_scolaire_form.save()
                return redirect('parametrage')
        elif 'cycle-form' in request.POST:
            cycle_form = CycleForm(request.POST)
            if cycle_form.is_valid():
                cycle_form.save()
                return redirect('parametrage')
        elif 'filiere-form' in request.POST:
            filiere_form = FiliereForm(request.POST)
            if filiere_form.is_valid():
                filiere_form.save()
                return redirect('parametrage')
        elif 'classe-form' in request.POST:
            classe_form = ClasseForm(request.POST)
            if classe_form.is_valid():
                classe_form.save()
                return redirect('parametrage')
        elif 'ue-form' in request.POST:
            ue_form = UnitEnseignementForm(request.POST)
            if ue_form.is_valid():
                ue_form.save()
                return redirect('parametrage')
        elif 'matiere-form' in request.POST:
            matiere_form = MatiereForm(request.POST)
            if matiere_form.is_valid():
                matiere_form.save()
                return redirect('parametrage')
    return render(request, 'initials/parametrage.html', context)
