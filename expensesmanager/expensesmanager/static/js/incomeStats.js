const renderChart = (data, labels) => {
  var ctx = document.getElementById("myChart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Income from the past year",
          data: data,
          backgroundColor: [
            "rgb(75, 192, 192)", //teal
            "rgb(255, 99, 132)", //pink
            "rgb(54, 162, 235)", //blue
            "rgb(255, 159, 64)", //orange
            "rgb(153, 102, 255)", //purple
            "rgb(255, 206, 86)", //yellow
          ],
        },
      ],
    },
    options: {
      plugins: {
        title: {
          display: true,
          text: "Income per source",
        },
      },
    },
  });
};

const getChartData = () => {
  console.log("fetching");
  fetch("/income/income-summary")
    .then((res) => res.json())
    .then((results) => {
      console.log(results);
      const source_data = results.income_source_data;
      const [labels, data] = [
        Object.keys(source_data),
        Object.values(source_data),
      ];

      renderChart(data, labels);
    });
};

document.onload = getChartData();
