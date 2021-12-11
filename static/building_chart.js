
var ctx = document.getElementById('myChart');
const info = {"other": 106,
    "relative": 236,
    "date": 221,
    "quantity_absolute": 122,
    "money": 266,
    "change": 84,
    "quantity_relative": 45,
    "absolute": 85,
    "product_number": 26
}
console.log(info)
const labels = Object.keys(info);
const data = {
    labels: labels,
    datasets: [
        {   
            label: 'Distribution of categories',
            data: Object.values(info),
            backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(255, 159, 64, 0.5)',
                'rgba(255, 205, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(201, 203, 207, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(153, 102, 255, 0.5)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)'
            ],
            borderWidth: 1
        }
    ]
};
Chart.defaults.color = "#fff";
Chart.borderColor = "#fff";

var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: {
        
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true
            }
        },
        scales: {
            
            xAxes: [{
              display: true,
              gridLines: {
                display: false,
                
              },
              scaleLabel: {
                display: true,
                labelString: 'Month',
                
              }
            }],
            yAxes: [{
              display: true,
              gridLines: {
                display: false
              },
              scaleLabel: {
                display: true,
                labelString: 'Value'
              }
            }]
          }
    }
});



