
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from apps.inscription_frais.forms import EleveForm,PaiementForm
from apps.maquette.models import Etudiant, Cycle, Filiere, Classe
from apps.inscription_frais.models import Paiement,RecuInscription
from django.http import JsonResponse, HttpResponse


def inscrire_eleve(request):
    form = EleveForm()
   

    if request.method == 'POST':
        eleve_form = EleveForm(request.POST)
        if eleve_form.is_valid():
            eleve_form.save()
            return redirect('recu_inscription')

    return render(request, 'secretaire/inscrire_eleve.html', {"form": form})

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


def recu_inscription(request):
    classe_id = request.GET.get('classe_id')
    etudiant_id = request.GET.get('etudiant_id')
    frais_inscription = request.GET.get('frais_inscription')

    classe = Classe.objects.get(id=classe_id)
    etudiant = Etudiant.objects.get(id=etudiant_id)

    nom_etudiant = etudiant.nom
    prenom_etudiant = etudiant.prenom

    recu = RecuInscription(classe=classe, etudiant=etudiant, frais_inscription=frais_inscription)
    recu.save()

    context = {
        'classe': classe,
        'nom_etudiant': nom_etudiant,
        'prenom_etudiant': prenom_etudiant,
        'frais_inscription': frais_inscription,
        'date': recu.date
    }
    return render(request, 'secretaire/recu_inscription.html', context)



def paiement(request):
   
        form = PaiementForm()
        if request.method == 'GET':
           return render(request, 'secretaire/paiement.html', {'form': form})

        if request.method == 'POST':
          form = PaiementForm(request.POST)
          if form.is_valid():
            etudiant = form.cleaned_data['etudiant']
            montant = form.cleaned_data['montant']
            # Obtenez d'autres données du formulaire

            # Enregistrez les détails du paiement dans la base de données
            paiement = Paiement(etudiant=etudiant, montant=montant)
            # Remplacez les champs ci-dessus par les champs réels de votre modèle de paiement
            paiement.save()

            # Redirigez vers la vue de détails du paiement avec l'ID du paiement
            return redirect('details_paiement', paiement_id=paiement.id)

        return render(request, 'secretaire/paiement.html', {'form': form})



def details_paiement(request, etudiant_id, classe_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    classe = Classe.objects.get(id=classe_id)
    paiements = Paiement.objects.filter(etudiant=etudiant, classe=classe)

    total_scolarite = classe.frais_scolarite
    total_paye = sum(p.montant_paye for p in paiements)

    context = {
        'etudiant': etudiant,
        'classe': classe,
        'paiements': paiements,
        'total_scolarite': total_scolarite,
        'total_paye': total_paye,
        'reste_payer': total_scolarite - total_paye,
    }

    return render(request, 'secretaire/details_paiement.html', context)



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
    

