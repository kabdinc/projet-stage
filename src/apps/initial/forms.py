from django import forms
from apps.maquette.models import Etablissement, AnneeAcademique, NiveauScolaire, Cycle, Filiere, Classe, UnitEnseignement, Matiere, Etudiant


class EtablissementForm(forms.ModelForm):
    class Meta:
        model = Etablissement
        fields = ['nom']


class AnneeAcademiqueForm(forms.ModelForm):
    class Meta:
        model = AnneeAcademique
        fields = ['libelle', 'date_debut', 'date_fin']
        
    widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }


class NiveauScolaireForm(forms.ModelForm):
    class Meta:
        model = NiveauScolaire
        fields = ['nom', 'etablissement']


class CycleForm(forms.ModelForm):
    class Meta:
        model = Cycle
        fields = ['nom', 'code', 'etablissement', 'AnneeAcademique']


class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['nom', 'code', 'cycle', 'AnneeAcademique']


class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['nom', 'code', 'filiere', 'AnneeAcademique']


class UnitEnseignementForm(forms.ModelForm):
    class Meta:
        model = UnitEnseignement
        fields = ['nom', 'code', 'credit', 'classe']


class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom', 'unit_ens', 'coefficient']


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['matricule','prenoms', 'nom', 'date_naissance']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }
