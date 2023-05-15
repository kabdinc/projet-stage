$(document).ready(function() {
    $('#id_cycle').change(function() {
      var cycleId = $(this).val();
      if (cycleId) {
        $.ajax({
          url: '/get_filieres/',
          data: {
            'cycle_id': cycleId
          },
          success: function(data) {
            $('#id_filiere').html(data);
            $('#id_classe').html('<option value="">-------</option>');
          }
        });
      } else {
        $('#id_filiere').html('<option value="">-------</option>');
        $('#id_classe').html('<option value="">-------</option>');
      }
    });
  
    $('#id_filiere').change(function() {
      var filiereId = $(this).val();
      if (filiereId) {
        $.ajax({
          url: '/get_classes/',
          data: {
            'filiere_id': filiereId
          },
          success: function(data) {
            $('#id_classe').html(data);
          }
        });
      } else {
        $('#id_classe').html('<option value="">-------</option>');
      }
    });
  });
  