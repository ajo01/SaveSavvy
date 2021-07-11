const renderChart = (data, labels) => {
  var ctx = document.getElementById("myChart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Expenses from the past year",
          data: data,
          backgroundColor: [
            "rgb(75, 192, 192)", //teal
            "rgb(255, 99, 132)", //pink
            "rgb(54, 162, 235)", //blue
            "rgb(255, 206, 86)", //yellow
            "rgb(255, 159, 64)", //orange
            "rgb(153, 102, 255)", //purple
          ],
        },
      ],
    },
    options: {
      plugins: {
        title: {
          display: true,
          text: "Expenses per category",
        },
      },
    },
  });
};

var ctx = document.getElementById("lineChart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "# of Votes",
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
          "rgb(75, 192, 192)", //teal
          "rgb(255, 99, 132)", //pink
          "rgb(54, 162, 235)", //blue
          "rgb(255, 206, 86)", //yellow
          "rgb(255, 159, 64)", //orange
          "rgb(153, 102, 255)", //purple
        ],
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

const getChartData = () => {
  fetch("/expense-summary")
    .then((res) => res.json())
    .then((results) => {
      console.log(results);
      const category_data = results.expense_category_data;
      const [labels, data] = [
        Object.keys(category_data),
        Object.values(category_data),
      ];

      renderChart(data, labels);
    });
};

document.onload = getChartData();
