from django import forms
from apps.maquette.models import Cycle, Filiere, Classe,Etudiant,AnneeAcademique
from apps.inscription_frais.models import  Paiement ,RecuInscription



from django import forms

class EleveForm(forms.ModelForm):
    cycle = forms.ModelChoiceField(queryset=Cycle.objects.all(), widget=forms.Select(attrs={'id': 'cycle', 'class': 'form-control'}))
    filiere = forms.ModelChoiceField(queryset=Filiere.objects.all(), widget=forms.Select(attrs={'id': 'filiere', 'data-url': '/get_filiere/', 'class': 'form-control'}))
    classe = forms.ModelChoiceField(queryset=Classe.objects.all(), widget=forms.Select(attrs={'id': 'classe', 'data-url': '/get_classe/', 'class': 'form-control'}))
    AnneeAcademique = forms.ModelChoiceField(queryset=AnneeAcademique.objects.all(), widget=forms.Select(attrs={'id': 'AneeAcademique', 'class': 'form-control'}))
    frais_inscription = forms.DecimalField(widget=forms.TextInput(attrs={'id': 'id_frais_inscription', 'class': 'form-control'}))
    matricule = forms.CharField(widget=forms.TextInput(attrs={
       'class': 'form-control',
       'id': 'matricule',
       'aria-describedby': 'matricule',
       'placeholder': 'Entrer le matricule',
    }))
    nom = forms.CharField(widget=forms.TextInput(attrs={
       'class': 'form-control',
       'id': 'nom',
       'aria-describedby': 'nom',
       'placeholder': 'Entrer le nom',
    }))
    
    prenoms = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'prenoms',
        'aria-describedby': 'prenoms',
        'placeholder': "Entrer le(s) prénom(s)",
    }))
    
    date_naissance = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'date_id',
        'aria-describedby': 'date',
        'type': 'Date',
        'placeholder': 'Entrer la date de naissance',
    }))
    
    class Meta:
        model = Etudiant
        fields = ['matricule','prenoms', 'nom', 'date_naissance', 'classe', 'AnneeAcademique']




class PaiementForm(forms.ModelForm):
    etudiant = forms.ModelChoiceField(
        queryset=Etudiant.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'autocomplete': 'on','id':'etudiant'}),
        
    )
    
    classe = forms.ModelChoiceField(queryset=Classe.objects.all(), widget=forms.Select(attrs={'id': 'classe', 'data-url': '/get_classe/',"class":"form-control"}))
   
    montant_paye= forms.DecimalField(widget=forms.TextInput(attrs={
      
      "class":"form-control" ,
        "id":"montant_id",
        "aria-describedby":"montant",
        "placeholder" : "Entrer le montant",
        
    
  
        
    })
       )
    class Meta:
        model = Paiement
        fields = ['etudiant', 'classe', 'montant_paye']
        # Vous pouvez personnaliser les widgets, les labels, etc. si nécessaire

class RecuInscriptionForm(forms.ModelForm):
    classe = forms.CharField(disabled=True)
    cycle = forms.CharField(disabled=True)
    filiere = forms.CharField(disabled=True)
    eleve = forms.CharField(disabled=True)

    class Meta:
        model = RecuInscription
        fields = ['classe', 'cycle', 'filiere', 'eleve', 'frais_inscription']
