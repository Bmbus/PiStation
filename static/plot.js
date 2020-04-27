var xlabels = []
var ydata = []

createPlot()

async function createPlot() {
    await getCsvData()
    console.log(xlabels)
    var ctx = document.getElementById('chart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xlabels,
            datasets: [{
                label: 'Humidity in Hours',
                data: ydata,
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
            console.log(hour)
            xlabels.push(hour)
            console.log(xlabels);
            
        }
        if (hum != undefined) {
            ydata.push(hum)
        }
    })
}