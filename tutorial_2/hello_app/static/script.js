// This is an example JavaScript code
// console.log("Hello from script.js!");
// document.write(2); // this may be stopping rest of code from running

// You can add more JavaScript code here
// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']}); // this isn't working at all

// Set a callback to run fxn after the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Emmy', 1],
    ['Rew & Sly', 2],
    ['Cap & Luna', 2]
  ]);

  // Set chart options
  var options = {'title':'Cats in our building',
                 'width':800,
                 'height':600};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}

// document.write(3);