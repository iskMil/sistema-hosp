const ctxCamas = document.getElementById('graficoCamas');

new Chart(ctxCamas, {
    type: 'doughnut',
    data: {
        labels: ['Disponibles', 'Ocupadas'],
        datasets: [{
            data: [camasDisponibles, camasOcupadas]
        }]
    }
});

const ctxEpidemiologia = document.getElementById('graficoEpidemiologia');

new Chart(ctxEpidemiologia, {
    type: 'bar',
    data: {
        labels: ['Dengue', 'Anemia'],
        datasets: [{
            label: 'Cantidad de casos',
            data: [casosDengue, casosAnemia]
        }]
    }
});









