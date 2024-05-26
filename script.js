document.addEventListener('DOMContentLoaded', function () {
    const labelFilter = document.getElementById('labelFilter');
    const tableRows = document.querySelectorAll('#talksTable tbody tr');

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
        tableRows.sort((rowA, rowB) => {
            const yearA = parseInt(rowA.querySelector('td:nth-child(3)').textContent);
            const yearB = parseInt(rowB.querySelector('td:nth-child(3)').textContent);
            return yearA - yearB;
        });
        // Remove existing rows
        while (tbody.firstChild) {
            tbody.removeChild(tbody.firstChild);
        }
        // Append sorted rows
        tableRows.forEach(row => tbody.appendChild(row));
    }

    populateFilterOptions();
    sortTable();
    labelFilter.addEventListener('change', filterTable);
});
