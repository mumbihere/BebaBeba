//function for updating the total at the top of dashboard
function updateTotals(){
    var url = '/api/totals/?format=json'
    $.getJSON(url,function(data){
        console.log(data);
        $( "#driver_total" ).html(data.drivers);
        $( "#passenger_total" ).html(data.passengers);
        $( "#booking_total" ).html(data.bookings);
        $( "#payment_total" ).html(data.payments);
    })
}




// Function for drawing the bottom column chart on the dashboard for last 5 months
function drawChart(highchartdiv){
    $.getJSON('/api/historical_data/?format=json', function (data) {

        // Create the chart
        var months = data.months;
        var datacount= data.monthly_counts;

        var options={
                        chart: {
                            renderTo: highchartdiv,
                            type: 'column'
                        },
                        title: {
                            text:'Dashboard: Last Five Months'
                        },
                        xAxis:{
                            categories: months,
                            title: {
                                // text: 'Metrics'
                            }
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: 'Values'
                            }
                        }, 
                        series:datacount
                   };

        var chart = new Highcharts.Chart(options);


    });

}

