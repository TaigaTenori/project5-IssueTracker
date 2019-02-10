var endpoint = '/api/data'
function generateGraphs() {
    $.ajax({
        method: 'GET',
        url: endpoint + "/month",
        success: function(response_data){
            displayChart(response_data, 'myChartMonth');
        },
        error: function(data) {
            console.log('error');
            console.log(data);
            
        }
    
    });
    
    $.ajax({
        method: "GET",
        url: endpoint + "/week",
        success: function (response_data){
            displayChart(response_data, 'myChartWeek');
        }
    });
}
function displayChart(response_data, chart_id){
    var ctx = document.getElementById(chart_id).getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [''],
            datasets: [
                
                {
                    label: '# of Issues',
                    
                    data: [response_data.data[0]],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255,99,132,1)',
                    borderWidth: 1
                },
                {
                    label: '# of Issues Resolved',
                    data: [response_data.data[1]],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                },
                {
                    label: "# of Issues being worked on",
                    data: [response_data.data[2]],
                    backgroundColor: 'rgba(255, 206, 86, 0.2)',
                    borderColor: 'rgba(255, 206, 86, 1)',
                    borderWidth: 1
                }
                
            ]
        },
        options: {
            legend: false,
            scales: {
                yAxes: [{
                     gridLines: {
                        offsetGridLines: false
                    },
                    ticks: {
                        beginAtZero:true
                    },

                }],
                xAxes: [{
                    stacked: false
            }],
            }
        }
    });  
}
