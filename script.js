document.addEventListener('DOMContentLoaded', function () {
    const labelFilter = document.getElementById('labelFilter');
    const tableRows = document.querySelectorAll('#papersTable tbody tr');

    function populateFilterOptions() {
        const labelSet = new Set();
        tableRows.forEach(row => {
            const labels = row.getAttribute('data-labels').split(', ');
            labels.forEach(label => labelSet.add(label));
        });
        labelSet.forEach(label => {
            const option = document.createElement('option');
            option.value = label;
            option.textContent = label;
            labelFilter.appendChild(option);
        });
    }

    function filterTable() {
        const selectedLabel = labelFilter.value;
        tableRows.forEach(row => {
            const labels = row.getAttribute('data-labels').split(', ');
            if (selectedLabel === 'all' || labels.includes(selectedLabel)) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    function sortTable() {
      const tbody = document.querySelector('#papersTable tbody');
      const rows = Array.from(tbody.querySelectorAll('tr'));

      rows.sort((a, b) => {
        const yearA = parseInt(a.cells[2].textContent, 10);
        const yearB = parseInt(b.cells[2].textContent, 10);
        return yearA - yearB;
      });

      rows.forEach(r => tbody.appendChild(r));
    }

    populateFilterOptions();
    sortTable();
    labelFilter.addEventListener('change', filterTable);
});
