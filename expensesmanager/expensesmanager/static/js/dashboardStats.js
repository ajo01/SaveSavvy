console.log("dashboardStats");
var ctx = document.getElementById("myChart").getContext("2d");
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
  fetch("/expense/expense-summary")
    .then((res) => res.json())
    .then((results) => {
      console.log(results);
      const expense_monthly_data = results.expense_month_data;
      const [labels, data] = [
        Object.keys(expense_monthly_data),
        Object.values(expense_monthly_data),
      ];
      fetch("/income/income-summary")
        .then((res) => res.json())
        .then((response) => {
          console.log(response);
          const income_monthly_data = results.income_month_data;
          const [incomeLabels, incomeData] = [
            Object.keys(income_monthly_data),
            Object.values(income_monthly_data),
          ];
          renderChart(data, labels);
        });
    });
};

document.onload = getChartData();
