// Testing whether API calls work using node.js

function fetchChartData() {
    // Make a fetch request to the API URL
    var apiUrl = 'https://archive-api.open-meteo.com/v1/archive?latitude=42.40001&longitude=-71.0&start_date=2022-01-01&end_date=2022-01-02&hourly=temperature_2m';

    fetch(apiUrl)
      .then(response => response.json())
      .then(apiData => {
        // Create an empty data array to store API data
        var data = [];

        // Add column headers to data array
        data.push(['Time', 'Temp']);
  
        // Populate the data array with API data
        apiData.hourly.time.forEach((time, index) => {
            var temperature = apiData.hourly.temperature_2m[index];
            data.push([time, temperature]);
        });
  
        // Log the content of the data array to the console
        console.log(data); // Log the entire data array

      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
}

console.log('Hello, Node.js!');

fetchChartData();
