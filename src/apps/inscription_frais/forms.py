from django import forms
from apps.maquette.models import Cycle, Filiere, Classe,Etudiant


from django import forms

class EleveForm(forms.ModelForm):
    cycle = forms.ModelChoiceField(queryset=Cycle.objects.all(), widget=forms.Select(attrs={'id': 'cycle'}))
    filiere = forms.ModelChoiceField(queryset=Filiere.objects.none(), widget=forms.Select(attrs={'id': 'filiere', 'data-url': '/get_filiere/'}))
    classe = forms.ModelChoiceField(queryset=Classe.objects.all(), widget=forms.Select(attrs={'id': 'classe', 'data-url': '/get_classe/'}))

    class Meta:
        model = Etudiant
        fields = ['nom', 'prenoms', 'date_naissance']

    
  
