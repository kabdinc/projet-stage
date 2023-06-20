
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.inscription_frais.forms import EleveForm,PaiementForm,RecuInscriptionForm
from apps.maquette.models import AnneeAcademique, Etudiant, Cycle, Filiere, Classe, Inscription
from apps.inscription_frais.models import Paiement,RecuInscription
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum



def inscrire_eleve(request):
     form = EleveForm() 
     if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            matricule = form.cleaned_data['matricule']
            prenoms = form.cleaned_data['prenoms']
            nom = form.cleaned_data['nom']
            date_naissance = form.cleaned_data['date_naissance']
            classe = form.cleaned_data['classe']
            annee_academique = form.cleaned_data['annee_academique']
            
            # Vérifier si l'étudiant existe déjà
            etudiant = Etudiant.objects.filter(matricule=matricule).first()
            if etudiant:
                # L'étudiant existe déjà, rediriger vers la vue de réinscription
                return redirect('reinscrire_eleve', etudiant_id=etudiant.id)
            
            # L'étudiant n'existe pas, création d'une nouvelle instance d'Etudiant et d'Inscription
            etudiant = Etudiant.objects.create(
                matricule=matricule,
                prenoms=prenoms,
                nom=nom,
                date_naissance=date_naissance
            )
            inscription = Inscription.objects.create(
                etudiant=etudiant,
                classe=classe,
                annee_academique=annee_academique
            )
            
            # Effectuer d'autres actions après l'inscription
            return redirect('recu_inscription', inscription_id=inscription.id)
            
        
    
    
     return render(request, 'secretaire/inscrire_eleve.html', {'form': form})

def selection_eleve(request):
    etudiants = Etudiant.objects.all()
    
    if request.method == 'POST':
        etudiant_id = request.POST.get('etudiant_id')
        if etudiant_id:
            return redirect('reinscrire_eleve', etudiant_id=etudiant_id)
    
    return render(request, 'secretaire/selection_eleve.html', {'etudiants': etudiants})
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EleveForm, FraisForm
from .models import Etudiant


def reinscrire_eleve(request, etudiant_id=None):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            classe = form.cleaned_data['classe']
            annee_academique = form.cleaned_data['annee_academique']
            
            # Mettre à jour l'inscription existante avec la nouvelle classe et l'année académique
            inscription = get_object_or_404(Inscription, etudiant=etudiant)
            inscription.classe = classe
            inscription.annee_academique = annee_academique
            inscription.save()
            
            # Effectuer d'autres actions après la réinscription
            
            return redirect('secretaire')
    else:
        initial_data = {
            'matricule': etudiant.matricule,
            'prenoms': etudiant.prenoms,
            'nom': etudiant.nom,
            'date_naissance': etudiant.date_naissance,
            'classe': etudiant.inscription.classe,
            'annee_academique': etudiant.inscription.annee_academique
        }
        form = EleveForm(initial=initial_data)
    
    return render(request, 'secretaire/reinscrire_eleve.html', {'form': form, 'etudiant_id': etudiant_id})



def get_filiere(request):
    cycle_id = request.GET.get('cycle_id')
    filieres = Filiere.objects.filter(cycle_id=cycle_id)
    return render(request, 'home/filiere_list.html', {'filieres': filieres})

def get_classe(request):
    filiere_id = request.GET.get('filiere_id')
    classes = Classe.objects.filter(filiere_id=filiere_id)
    return render(request, 'home/classe_list.html', {'classes': classes})




def get_frais_inscription(request):
    classe_id = request.GET.get('classe_id')
    classe = Classe.objects.filter(id=classe_id).first()
    montant = classe.frais_inscription if classe else None
    return JsonResponse({'montant': str(montant)})


   
def recu_inscription(request, inscription_id):
    # Récupérer l'objet Inscription à partir de l'ID
    inscription = Inscription.objects.get(id=inscription_id)
    
    # Récupérer l'étudiant associé à l'inscription
    etudiant = inscription.etudiant
    
    context = {
        'inscription': inscription,
        'etudiant': etudiant,
    }
    
    return render(request, 'secretaire/recu_inscription.html', context)

   


def paiement(request):
    if request.method == 'POST':
        form = PaiementForm(request.POST)
        if form.is_valid():
            etudiant = form.cleaned_data['etudiant']
            classe = form.cleaned_data['classe']
            montant = form.cleaned_data['montant_paye']

            # Enregistrez les détails du paiement dans la base de données
            paiement = Paiement(etudiant=etudiant, classe=classe, montant_paye=montant)
            paiement.save()

            # Redirigez vers la vue de détails du paiement avec l'ID de l'étudiant et de la classe
            return redirect('details_paiement', paiement_id=paiement.id ,etudiant_id=etudiant.id, classe_id=classe.id)
    else:
        form = PaiementForm()

    return render(request, 'secretaire/paiement.html', {'form': form})





def get_classe_details(request):
    etudiant_id = request.GET.get('etudiant_id')
    classe = Classe.objects.filter(etudiant_id=etudiant_id).first()

    if classe:
        classe_details = {
            'nom': classe.nom,
           
            # Ajoutez d'autres champs que vous souhaitez récupérer
        }
        return JsonResponse(classe_details)
    else:
        return JsonResponse({'error': 'Classe non trouvée'})
    

def liste_etudiant(request):
    etudiants = Etudiant.objects.all()
    context = {
        'etudiants': etudiants
    }
    return render(request, 'daf/liste_etudiant.html', context)


def etat_paiement(request, etudiant_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    inscription = Inscription.objects.get(etudiant=etudiant)
    paiements = Paiement.objects.filter(etudiant=etudiant)

    total_paye = paiements.aggregate(Sum('montant_paye'))['montant_paye__sum']
    frais_scolarite = inscription.classe.frais_scolarite
    reste_a_payer = frais_scolarite - total_paye if total_paye else frais_scolarite

    context = {
        'etudiant': etudiant,
        'classe': inscription.classe,
        'frais_scolarite': frais_scolarite,
        'paiements': paiements,
        'total_paye': total_paye,
        'reste_a_payer': reste_a_payer
    }

    return render(request, 'daf/etat_paiement.html', context)


def gestion_inscription_frais(request):
   
    return render(request, 'daf/gestion_inscription_frais.html')

def liste_classes(request):
    classes = Classe.objects.all()
    context = {'classes': classes}
    return render(request, 'daf/liste_classes.html', context)

def modifier_frais(request, classe_id):
    classe = Classe.objects.get(id=classe_id)
    form = FraisForm(instance=classe)

    if request.method == 'POST':
        form = FraisForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('liste_classes')

    context = {'form': form}
    return render(request, 'daf/modifier_frais.html', context)

def details_paiement(request, etudiant_id, classe_id, paiement_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    classe = Classe.objects.get(id=classe_id)
    paiement = Paiement.objects.get(id=paiement_id)
    montant_paye = paiement.montant_paye

    total_scolarite = classe.frais_scolarite
    total_paye = Paiement.objects.filter(etudiant=etudiant, classe=classe).aggregate(Sum('montant_paye'))['montant_paye__sum']
    reste_payer = total_scolarite - total_paye

    context = {
        'etudiant': etudiant,
        'classe': classe,
        'paiement': paiement,
        'total_scolarite': total_scolarite,
        'total_paye': total_paye,
        'reste_payer': reste_payer,
        'montant_paye': montant_paye,
    }

    return render(request, 'daf/details.paiement.html', context)
