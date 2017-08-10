
// Function for drawing the bottom column chart
function drawChart(highchartdiv){
    $.getJSON('https://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?', function (data) {

        // Create the chart
        var answers = ['January','February' ,'March', 'April','May'];
        var answer_counts= [
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
                            categories: answers,
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
                        series:answer_counts
                   };

        var chart = new Highcharts.Chart(options);


    });

}

