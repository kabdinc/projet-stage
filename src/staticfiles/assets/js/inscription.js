document.addEventListener('DOMContentLoaded', function() {
  function updateFraisInscription() {
      var classeId = document.getElementById('classe').value;
      var fraisInscriptionElement = document.getElementById('id_frais_inscription');

      var xhr = new XMLHttpRequest();
      xhr.open('GET', '/get_frais_inscription/?classe_id=' + classeId, true);
      xhr.onload = function() {
          if (xhr.status === 200) {
              fraisInscriptionElement.innerHTML = xhr.responseText;
          } else {
              fraisInscriptionElement.innerHTML = '';
          }
      };
      xhr.onerror = function() {
          fraisInscriptionElement.innerHTML = '';
      };
      xhr.send();
  }

  // Appeler la fonction updateFraisInscription() lorsque la valeur de la classe change
  document.getElementById('classe').addEventListener('change', updateFraisInscription);
});
