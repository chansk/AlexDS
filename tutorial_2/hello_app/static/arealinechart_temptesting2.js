// Goal: Get historical data plotting dynamically on website
// Secondary: change time to string, where discrete plotting is possible, for x-ticks to work

// Uncomment these two lines when testing in browser, comment out when testing locally
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(fetchChartData);

// // ATTENTION: this works
function fetchChartData() {
    // Make a fetch request to the API URL
    var apiUrl = 'https://archive-api.open-meteo.com/v1/archive?latitude=42.40001&longitude=-71.0&start_date=2022-01-01&end_date=2022-01-02&hourly=temperature_2m';

    fetch(apiUrl)
      .then(response => response.json())
      .then(apiData => {
        // Create an empty data array to store API data
        var data = [];
  
        // Populate the data array with API data
        apiData.hourly.time.forEach((time, index) => {
            var temperature = apiData.hourly.temperature_2m[index];
            var dateParts = time.split('T')[0].split('-'); // Split date and time
            var timeParts = time.split('T')[1].split(':');
            var date = new Date(
                dateParts[0], // Year
                parseInt(dateParts[1]) - 1, // Month (subtract 1 since months are zero-based)
                dateParts[2], // Day
                timeParts[0], // Hour
                timeParts[1]  // Minute
            );
            data.push([date, temperature]);
        });
  
        // Log the content of the data array to the console
        console.log(data); // Log the entire data array
      
        // Call drawChart with the data array
        drawChart(data);

      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
}

function drawChart(data) {
    var dataArray = [['Time', 'Temp']].concat(data); // Add header row

    // Initialize dataTable using the original dataArray
    var dataTable = google.visualization.arrayToDataTable(dataArray);

    var options = {
        title: 'Temp (C) at 42.4, -71.0, Jan 1 to Jan 2, 2022',
        hAxis: {title: 'Time',  titleTextStyle: {color: '#333'}}, // x-axis label
        vAxis: {title: 'Temperature', minValue: 0} // y-axis label and options
    };

    // Initialize chart as a variable for plotting
    var chart = new google.visualization.AreaChart(document.getElementById('chart_div_area'));
    chart.draw(dataTable, options);
}