$(document).ready(function() {
  $('#filiere').change(function() {
    var filiere_id = $(this).val();
    if (filiere_id) {
      $.ajax({
        url: '/get_classe/',
        data: {
          'filiere_id': filiere_id
        },
        dataType: 'json',
        success: function(data) {
          $('#classe').empty();
          if (data.length > 0) {
            $.each(data, function(index, value) {
              $('#classe').append('<option value="' + value + '">' + value + '</option>');
            });
          } else {
            $('#classe').append('<option value="">Aucune classe disponible</option>');
          }
        }
      });
    } else {
      $('#classe').empty();
      $('#classe').append('<option value="">Sélectionner une filière </option>');
    }
  });
});
