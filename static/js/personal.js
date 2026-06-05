console.log("Nombres:", nombresPersonal);
console.log("Atenciones:", atencionesPersonal);

const ctxPersonal = document.getElementById('graficoPersonal');

new Chart(ctxPersonal, {
    type: 'bar',
    data: {
        labels: nombresPersonal,
        datasets: [{
            label: 'Atenciones realizadas',
            data: atencionesPersonal,
            backgroundColor: '#1565c0'
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});