<template>
  <div>
    <h2>Firebase vue Startup kit</h2>
    <div class="chart-container">
      <div id="myDiv"></div> <!-- Bar chart will be drawn inside this div -->
      <div id="myDivPie"></div> <!-- Pie chart will be drawn inside this div -->
    </div>
  </div>
</template>

<style scoped>
.chart-container {
  display: flex;
  justify-content: space-around; /* Optional. This adds some space between the charts */
}
</style>

<script>
import Plotly from 'plotly.js-dist';

export default {
  name: 'Top',
  mounted() {
    // Bar chart data and layout
    let barData = [{
      x: ['Category 1', 'Category 2', 'Category 3'], // Replace with your actual data
      y: [10, 15, 7], // Replace with your actual data
      type: 'bar'
    }];

    let barLayout = {
      title: 'Bar Chart',
      width: 500,
      height: 500
    };

    Plotly.newPlot('myDiv', barData, barLayout);
    
    // Pie chart data and layout
    let pieData = [{
      values: [19, 26, 55], // Replace with your actual data
      labels: ['Residential', 'Non-Residential', 'Utility'], // Replace with your actual data
      type: 'pie'
    }];

    let pieLayout = {
      title: 'Pie Chart',
      height: 400,
      width: 500
    };

    Plotly.newPlot('myDivPie', pieData, pieLayout);
  },
};
</script>

