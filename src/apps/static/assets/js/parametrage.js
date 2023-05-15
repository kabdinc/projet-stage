$(document).ready(function() {

    // Cacher tous les formulaires
    $('#etablissement-form, #annee-academique-form, #niveau-scolaire-form, #cycle-form, #filiere-form, #classe-form, #ue-form, #matiere-form').hide();
  
    // Afficher le formulaire d'ajout d'établissement
    $('#add-etablissement').click(function() {
      $('#etablissement-form').show();
    });
  
    // Afficher le formulaire d'ajout d'année académique
    $('#add-annee-academique').click(function() {
      $('#annee-academique-form').show();
    });
  
    // Afficher le formulaire d'ajout de niveau scolaire
    $('#add-niveau-scolaire').click(function() {
      $('#niveau-scolaire-form').show();
    });
  
    // Afficher le formulaire d'ajout de cycle
    $('#add-cycle').click(function() {
      $('#cycle-form').show();
    });
  
    // Afficher le formulaire d'ajout de filière
    $('#add-filiere').click(function() {
      $('#filiere-form').show();
    });
  
    // Afficher le formulaire d'ajout de classe
    $('#add-classe').click(function() {
      $('#classe-form').show();
    });
  
    // Afficher le formulaire d'ajout d'unité d'enseignement
    $('#add-ue').click(function() {
      $('#ue-form').show();
    });
  
    // Afficher le formulaire d'ajout de matière
    $('#add-matiere').click(function() {
      $('#matiere-form').show();
    });
  });
  