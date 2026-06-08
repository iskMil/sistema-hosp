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
        labels: ['Dengue', 'Neumonía'],
        datasets: [{
            label: 'Cantidad de casos',
            data: [casosDengue, casosAnemia]
        }]
    }
});









