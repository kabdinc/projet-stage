
import logging
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from apps.authentication.forms import AllouerMatiereForm, EnseignantForm
from apps.authentication.models import Intervenant
from apps.maquette.models import Etablissement, AnneeAcademique, NiveauScolaire, Cycle, Filiere, Classe, UnitEnseignement, Matiere
from .forms import EtablissementForm, AnneeAcademiqueForm, NiveauScolaireForm, CycleForm, FiliereForm, ClasseForm, UnitEnseignementForm, MatiereForm

def parametrage(request):
   
    return render(request, 'initials/parametrage.html')


def gestion_etablissement(request):
   
    return render(request, 'initials/gestion_etablissement.html')

def liste_etablissements(request):
    etablissements = Etablissement.objects.all()
    context = {
        'etablissements': etablissements
    }
    return render(request, 'initials/liste_etablissements.html', context)

def gestion_cycle(request):
    cycles = Cycle.objects.all()
    context = {
        'cycles': cycles
    }
    return render(request, 'initials/gestion_cycle.html', context)


def gestion_filiere(request):
    filieres = Filiere.objects.all()
    context = {
        'filieres': filieres
    }
    return render(request, 'initials/gestion_filiere.html', context)

def gestion_classe(request):
    classes = Classe.objects.all()
    context = {
        'classes': classes
    }
    return render(request, 'initials/gestion_classe.html', context)

def gestion_ue(request):
    unitenseignements = UnitEnseignement.objects.all()
    context = {
        'unitenseignements': unitenseignements
    }
    return render(request, 'initials/gestion_ue.html', context)


def gestion_matiere(request):
    matieres = Matiere.objects.all()
    context = {
        'matieres': matieres
    }
    return render(request, 'initials/gestion_matiere.html', context)


def create_niveau_scolaire(request):
    if request.method == 'POST':
        form = NiveauScolaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parametrage')  # Rediriger vers la liste des niveaux scolaires
    else:
        form = NiveauScolaireForm()
    return render(request, 'initials/creer_niveau_scolaire.html', {'form': form})

def update_niveau_scolaire(request, niveau_scolaire_id):
    niveau_scolaire = NiveauScolaire.objects.get(id=niveau_scolaire_id)
    if request.method == 'POST':
        form = NiveauScolaireForm(request.POST, instance=niveau_scolaire)
        if form.is_valid():
            form.save()
            return redirect('parametrage')  # Rediriger vers la liste des niveaux scolaires
    else:
        form = NiveauScolaireForm(instance=niveau_scolaire)
    return render(request, 'initials/modifier_niveau_scolaire.html', {'form': form})

def delete_niveau_scolaire(request, niveau_scolaire_id):
    niveau_scolaire = NiveauScolaire.objects.get(id=niveau_scolaire_id)
    niveau_scolaire.delete()
    return redirect('parametrage')  # Rediriger vers la liste des niveaux scolaires

def create_etablissement(request):
    if request.method == 'POST':
        form = EtablissementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parametrage')  # Rediriger vers la liste des établissements
    else:
        form = EtablissementForm()
    return render(request, 'initials/creer_etablissement.html', {'form': form})

def update_etablissement(request, etablissement_id):
    etablissement = Etablissement.objects.get(id=etablissement_id)
    if request.method == 'POST':
        form = EtablissementForm(request.POST, instance=etablissement)
        if form.is_valid():
            form.save()
            return redirect('parametrage')  # Rediriger vers la liste des établissements
    else:
        form = EtablissementForm(instance=etablissement)
    return render(request, 'initials/modifier_etablissement.html', {'form': form})

def delete_etablissement(request, etablissement_id):
    etablissement = Etablissement.objects.get(id=etablissement_id)
    etablissement.delete()
    return redirect('parametrage')  # Rediriger vers la liste des établissements



def create_cycle(request):
    if request.method == 'POST':
        form = CycleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parametrage')  # Rediriger vers la liste des cycles
    else:
        form = CycleForm()
    return render(request, 'initials/creer_cycle.html', {'form': form})

def update_cycle(request, cycle_id):
    cycle = Cycle.objects.get(id=cycle_id)
    if request.method == 'POST':
        form = CycleForm(request.POST, instance=cycle)
        if form.is_valid():
            form.save()
            return redirect('parametrage')  # Rediriger vers la liste des cycles
    else:
        form = CycleForm(instance=cycle)
    return render(request, 'initials/modifier_cycle.html', {'form': form})

def delete_cycle(request, cycle_id):
    cycle = Cycle.objects.get(id=cycle_id)
    cycle.delete()
    return redirect('parametrage')  # Rediriger vers la liste des cycles



def create_filiere(request):
    if request.method == 'POST':
        form = FiliereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parametrage')
    else:
        form = FiliereForm()
    return render(request, 'initials/creer_filiere.html', {'form': form})

def update_filiere(request, filiere_id):
    filiere = Filiere.objects.get(id=filiere_id)
    if request.method == 'POST':
        form = FiliereForm(request.POST, instance=filiere)
        if form.is_valid():
            form.save()
            return redirect('parametrage')
    else:
        form = FiliereForm(instance=filiere)
    return render(request, 'initials/modifier_filiere.html', {'form': form})

def delete_filiere(request, filiere_id):
    filiere = Filiere.objects.get(id=filiere_id)
    filiere.delete()
    return redirect('parametrage')

def create_classe(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parametrage')
    else:
        form = ClasseForm()
    return render(request, 'initials/creer_classe.html', {'form': form})

def update_classe(request, classe_id):
    classe = Classe.objects.get(id=classe_id)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('parametrage')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'initials/modifier_classe.html', {'form': form})

def delete_classe(request, classe_id):
    classe = Classe.objects.get(id=classe_id)
    classe.delete()
    return redirect('parametrage')

def create_unit_enseignement(request):
    if request.method == 'POST':
        form = UnitEnseignementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parametrage')
    else:
        form = UnitEnseignementForm()
    return render(request, 'initials/creer_ue.html', {'form': form})

def update_unit_enseignement(request, unitenseignement_id):
    unitenseignement = UnitEnseignement.objects.get(id=unitenseignement_id)
    if request.method == 'POST':
        form = UnitEnseignementForm(request.POST, instance=unitenseignement)
        if form.is_valid():
            form.save()
            return redirect('parametrage')
    else:
        form = UnitEnseignementForm(instance=unitenseignement)
    return render(request, 'initials/modifier_ue.html', {'form': form})

def delete_unit_enseignement(request, unit_enseignement_id):
    unit_enseignement = UnitEnseignement.objects.get(id=unit_enseignement_id)
    unit_enseignement.delete()
    return redirect('parametrage')

def create_matiere(request):
    if request.method == 'POST':
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parametrage')
    else:
        form = MatiereForm()
    return render(request, 'initials/creer_matiere.html', {'form': form})

def update_matiere(request, matiere_id):
    matiere = Matiere.objects.get(id=matiere_id)
    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('parametrage')
    else:
        form = MatiereForm(instance=matiere)
    return render(request, 'initials/modifier_matiere.html', {'form': form})

def delete_matiere(request, matiere_id):
    matiere = Matiere.objects.get(id=matiere_id)
    matiere.delete()
    return redirect('parametrage')





def gestion_enseignant(request):
    enseignants = Intervenant.objects.filter(type_user__name='ENSEIGNANT')

    context = {
        'enseignants': enseignants
    }
    return render(request, 'initials/gestion_enseignant.html', context)


logger = logging.getLogger(__name__)

def creer_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            enseignant = form.save(commit=False)
            type_user = form.cleaned_data['type_user']
           
            enseignant.save()
            enseignant.type_user.add(type_user)  # Lie l'enseignant au type_user "ENSEIGNANT"
           
            return redirect('home')
    else:
        form = EnseignantForm()
    return render(request, 'initials/creer_enseignant.html', {'form': form})



def modifier_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Intervenant, id=enseignant_id)

    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('gestion_enseignant')
    else:
        form = EnseignantForm(instance=enseignant)

    return render(request, 'initials/modifier_enseignant.html', {'form': form})

def delete_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Intervenant, id=enseignant_id)
    enseignant.delete()
    return redirect('gestion_enseignant')

    
def associer_matiere(request, enseignant_id):
    enseignant = Intervenant.objects.get(id=enseignant_id)
    
    if request.method == 'POST':
        form = AllouerMatiereForm(request.POST)
        if form.is_valid():
            matieres = form.cleaned_data['matieres']
            enseignant.matieres.set(matieres)
            enseignant.save()
            return redirect('gestion_enseignant')
    else:
        initial_data = {
            'first_name': enseignant.first_name,
            'last_name': enseignant.last_name
        }
        form = AllouerMatiereForm(initial=initial_data)
    
    context = {
        'form': form,
        'enseignant': enseignant,
    }
    return render(request, 'initials/allouer_matiere.html', context)

