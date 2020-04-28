var xlabels_hum_today = []
var ylabels_hum_today = []
//var xlabels_hum_week = []
//var ylabels_hum_week = []
//var xlabels_hum_all = []
//var ylabels_hum_all = []

humidityPlotToday()

async function humidityPlotToday() {
    await getCsvData()
    console.log(xlabels_hum_today)
    var ctx = document.getElementById('chart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xlabels_hum_today,
            datasets: [{
                label: 'Humidity in Hours',
                data: ylabels_hum_today,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

async function getCsvData() {
    const response = await fetch("static/csv/data.csv")
    const data = await response.text()
    const table = data.split("\n").slice(1)
    table.forEach(row => {
        const columns = row.split(",")
        const hum = columns[0]
        const temp = columns[1]
        const timestamp = columns[2]
        if (timestamp != undefined) {
            const hour = timestamp.split(" ")[1].split(":")[0]
            if (xlabels_hum_today.includes(hour) != true) {
                xlabels_hum_today.push(hour)
            } // TODO durchschnitt für gleiche uhrzeit ausrechnen
        }
        if (hum != undefined) {
            ylabels_hum_today.push(hum)
        }

    })
}