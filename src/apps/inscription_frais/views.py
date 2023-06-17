
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from apps.inscription_frais.forms import EleveForm,PaiementForm,RecuInscriptionForm
from apps.maquette.models import Etudiant, Cycle, Filiere, Classe
from apps.inscription_frais.models import Paiement,RecuInscription
from django.http import JsonResponse, HttpResponse

from django.shortcuts import redirect

def inscrire_eleve(request):
    form = EleveForm()

    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            etudiant = form.save()  # Enregistrer l'étudiant dans la base de données
            print("Enregistrement réussi !")
            
            # Rediriger l'utilisateur vers la page recu_inscription
            return redirect('recu_inscription', etudiant_id=etudiant.id)
        else:
            print(form.errors)
    
    return render(request, 'secretaire/inscrire_eleve.html', {'form': form})


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

def recu_inscription(request, etudiant_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    classe = etudiant.classe
    filiere = classe.filiere
    cycle = filiere.cycle
    initial_data = {
        'classe': classe.nom,
        'cycle': cycle.nom,
        'filiere': filiere.nom,
        'eleve': etudiant.__str__(),
        'frais_inscription': classe.frais_inscription
    }
    form = RecuInscriptionForm(initial=initial_data)

    if request.method == 'POST':
        form = RecuInscriptionForm(request.POST)
        if form.is_valid():
            recu = form.save(commit=False)
            recu.classe = classe
            recu.eleve = etudiant
            recu.save()
            # Autres actions à effectuer après l'enregistrement

    return render(request, 'secretaire/recu_inscription.html', {'etudiant': etudiant, 'form': form})


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
            return redirect('details_paiement', etudiant_id=etudiant.id, classe_id=classe.id)
    else:
        form = PaiementForm()

    return render(request, 'secretaire/paiement.html', {'form': form})


def details_paiement(request, etudiant_id, classe_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    classe = Classe.objects.get(id=classe_id)
    paiements = Paiement.objects.filter(etudiant=etudiant, classe=classe)

    total_scolarite = classe.frais_scolarite
    total_paye = sum(p.montant_paye for p in paiements)

    reste_payer = total_scolarite - total_paye

    context = {
        'etudiant': etudiant,
        'classe': classe,
        'paiements': paiements,
        'total_scolarite': total_scolarite,
        'total_paye': total_paye,
        'reste_payer': reste_payer,
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
    

