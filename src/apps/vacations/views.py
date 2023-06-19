from django.shortcuts import get_object_or_404, render, redirect
from apps.authentication.models import Intervenant




def gestion_vacations(request):
   
    return render(request, 'daf/gestion_vacations.html')

def enseignant_per(request):
    enseignants_per = Intervenant.objects.filter(statut='permanent')

    if request.method == 'POST':
        for enseignant in enseignants_per:
            salaire = request.POST.get(f"salaire_{enseignant.id}")
            enseignant.salaire = salaire
            enseignant.save()

        return redirect('enseignant_per')

    context = {
        'enseignants_per': enseignants_per
    }

    # Pré-remplir le salaire de chaque enseignant dans le contexte
    for enseignant in enseignants_per:
        context[f"salaire_{enseignant.id}"] = enseignant.salaire

    return render(request, 'daf/enseignant_perm.html', context)

def enseignant_vac(request):
    enseignants_vac = Intervenant.objects.filter(statut='vacataire')
    if request.method == 'POST':
        for enseignant in enseignants_vac:
            taux_horaire = request.POST.get(f"taux_horaire_{enseignant.id}")
            enseignant.taux_horaire = taux_horaire
            enseignant.save()

        return redirect('enseignant_vac')

    context = {
        'enseignants_vac': enseignants_vac
    }

    for enseignant in enseignants_vac:
        context[f"taux_horaire_{enseignant.id}"] = enseignant.taux_horaire

  
    return render(request, 'daf/enseignant_vac.html', context)

def modifier_taux_horaire(request, enseignant_id):
    enseignant = Intervenant.objects.get(id=enseignant_id)

    if request.method == 'POST':
        taux_horaire = request.POST.get('taux_horaire')
        enseignant.taux_horaire = taux_horaire
        enseignant.save()
        return redirect('enseignant_vac')

    context = {
        'enseignant': enseignant
    }

    return render(request, 'daf/modifier_taux_horaire.html', context)



def frais_vacations(request, enseignant_id):
    enseignant = get_object_or_404(Intervenant, pk=enseignant_id)
    matieres = enseignant.matieres.all()
    taux_horaire = enseignant.taux_horaire

    frais_vacations = []
    total_vacations = 0

    for matiere in matieres:
        volume_horaire = matiere.volume_horaire
        frais_vacation = volume_horaire * taux_horaire
        frais_vacations.append((matiere, volume_horaire, frais_vacation))
        total_vacations += frais_vacation

    context = {
        'enseignant': enseignant,
        'taux_horaire': taux_horaire,
        'frais_vacations': frais_vacations,
        'total_vacations': total_vacations
    }

    return render(request, 'daf/frais_vacations.html', context)

from django.shortcuts import render
from .models import Intervenant

def totaux_vacations(request):
    enseignants_vacataires = Intervenant.objects.filter(statut='vacataire')
    frais_enseignants = []
    total_frais = 0

    for enseignant in enseignants_vacataires:
        matieres = enseignant.matieres.all()
        taux_horaire = enseignant.taux_horaire
        frais_total = 0

        for matiere in matieres:
            volume_horaire = matiere.volume_horaire
            frais_vacation = volume_horaire * taux_horaire
            frais_total += frais_vacation

        frais_enseignants.append((enseignant, frais_total))
        total_frais += frais_total

    context = {
        'frais_enseignants': frais_enseignants,
        'total_frais': total_frais
    }

    return render(request, 'daf/totaux_vacations.html', context)
