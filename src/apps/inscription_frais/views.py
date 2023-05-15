
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from apps.inscription_frais.forms import EleveForm
from apps.maquette.models import Etudiant, Cycle, Filiere, Classe
from django.http import JsonResponse

def inscrire_eleve(request):
    form = EleveForm()
   

    if request.method == 'POST':
        eleve_form = EleveForm(request.POST)
        if eleve_form.is_valid():
            eleve_form.save()
            return HttpResponseRedirect('/')

    return render(request, 'home/inscrire_eleve.html', {"form": form})

def get_filiere(request):
    cycle_id = request.GET.get('cycle_id')
    filieres = Filiere.objects.filter(cycle_id=cycle_id).values_list('nom', flat=True)
    return JsonResponse(list(filieres), safe=False)

def get_classe(request):
    filiere_id = request.GET.get('filiere_id')
    filiere = get_object_or_404(Filiere, id=filiere_id)
    classes = Classe.objects.filter(filiere=filiere).values_list('nom', flat=True)
    return JsonResponse(list(classes), safe=False)
