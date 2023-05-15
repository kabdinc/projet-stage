document.getElementById('cycle').addEventListener('change', function() {
  const cycleId = this.value;
  const filiereSelect = document.getElementById('filiere');
  const classeSelect = document.getElementById('classe');
  filiereSelect.innerHTML = '<option value="">---------</option>';
  classeSelect.innerHTML = '<option value="">---------</option>';
  if (cycleId) {
      const url = '/get_filiere/?cycle_id=' + cycleId;
      fetch(url)
          .then((response) => response.json())
          .then((data) => {
              for (const filiere of data) {
                  const option = document.createElement('option');
                  option.value = filiere.id;
                  option.text = filiere.nom;
                  filiereSelect.appendChild(option);
              }
          });
  }
});
