<template>
  <div>
    <h2>Firebase vue Startup kit</h2>
    <label>
      <input type="radio" value="bar" v-model="chartType"> Bar Chart
    </label>
    <label>
      <input type="radio" value="pie" v-model="chartType"> Pie Chart
    </label>
    <label>
      <input type="radio" value="line" v-model="chartType"> Line Chart
    </label>
    <div class="chart-container">
      <div id="myDiv" v-show="chartType === 'bar'"></div>
      <div id="myDivPie" v-show="chartType === 'pie'"></div>
      <div id="myDivLine" v-show="chartType === 'line'"></div>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist';
import { ref, watch, onMounted } from 'vue';

export default {
  name: 'Top',
  setup() {
    const chartType = ref('bar');

    onMounted(() => {
      renderCharts();
    });
    
    watch(chartType, ()=>{
      renderCharts();
    })

    const renderCharts = () => {
      if(chartType.value === 'bar') {
        let barData = [{
          x: ['Category 1', 'Category 2', 'Category 3'],
          y: [10, 15, 7],
          type: 'bar'
        }];

        let barLayout = {
          title: 'Bar Chart',
          width: 500,
          height: 500
        };

        Plotly.newPlot('myDiv', barData, barLayout);
      }
      
      if(chartType.value === 'pie') {
        let pieData = [{
          values: [19, 26, 55],
          labels: ['Residential', 'Non-Residential', 'Utility'],
          type: 'pie'
        }];

        let pieLayout = {
          title: 'Pie Chart',
          height: 400,
          width: 500
        };

        Plotly.newPlot('myDivPie', pieData, pieLayout);
      }

      if(chartType.value === 'line') {
        let lineData = [{
          x: [1, 2, 3, 4],
          y: [10, 15, 13, 17],
          mode: 'lines'
        }];

        let lineLayout = {
          title: 'Line Chart',
          height: 400,
          width: 500
        };

        Plotly.newPlot('myDivLine', lineData, lineLayout);
      }
    };

    return {
      chartType
    };
  }
};
</script>

<style scoped>
.chart-container {
  display: flex;
  justify-content: space-around;
}
</style>
