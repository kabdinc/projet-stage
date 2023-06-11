
    $(document).ready(function() {
        $('#id_classe').change(function() {
            var classeId = $(this).val();

            $.ajax({
                url: '/get_frais_inscription/',
                data: {
                    'classe_id': classeId
                },
                dataType: 'json',
                success: function(response) {
                    $('#id_frais_inscription').val(response.frais_inscription);
                },
                error: function() {
                    alert("Une erreur s'est produite lors de la récupération des frais d'inscription.");
                }
            });
        });
    });


