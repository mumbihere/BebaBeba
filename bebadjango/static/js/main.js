//function for updating the total at the top of dashboard
function updateTotals(){
    var url = 'http://127.0.0.1:8000/api/totals/?format=json'
    $.getJSON(url,function(data){
        console.log(data);
        $( "#driver_total" ).html(data.drivers);
        $( "#passenger_total" ).html(data.passengers);
        $( "#booking_total" ).html(data.bookings);
        $( "#payment_total" ).html(data.payments);



    })
}




// Function for drawing the bottom column chart on the dashboard
function drawChart(highchartdiv){
    $.getJSON('https://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?', function (data) {

        // Create the chart
        var months = ['January','February' ,'March', 'April','May'];
        var datacount= [
                    {name: 'Passengers', data : [2,1,0,2,5]},
                    {name: 'Bookings', data: [2,4,3,1,3]},
                    {name: 'Drivers', data: [2,2,1,4,2]},
                    {name: 'Payments', data: [4,3,6,1,3]} 

                    ];


        var options={
                        chart: {
                            renderTo: highchartdiv,
                            type: 'column'
                        },
                        title: {
                            text:'Dashboard'
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

