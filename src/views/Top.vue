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
    <button v-on:click="test">Test</button>
    <div class="chart-container">
      <Plotly :data="chartData" :layout="chartLayout" :display-mode-bar="false" />
    </div>
  </div>
</template>

<script>
import { Plotly } from 'vue-plotly';
import { ref, watch, onMounted } from 'vue';

export default {
  components: {
    Plotly,
  },
  name: 'Top',
  setup() {
    const chartType = ref('');
    const chartData = ref({});
    const chartLayout = ref({});

    watch(chartType, ()=>{
      updateChart();
    })

    onMounted(() => {
      chartType.value = 'bar';
    });

    const updateChart = () => {
      if(chartType.value === 'bar') {
        chartData.value = [{
          x: ['Category 1', 'Category 2', 'Category 3'],
          y: [10, 15, 7],
          type: 'bar'
        }];

        chartLayout.value = {
          title: 'Bar Chart',
          width: 500,
          height: 500
        };
      }
      
      if(chartType.value === 'pie') {
        chartData.value = [{
          values: [19, 26, 55],
          labels: ['Residential', 'Non-Residential', 'Utility'],
          type: 'pie'
        }];

        chartLayout.value = {
          title: 'Pie Chart',
          height: 400,
          width: 500
        };
      }

      if(chartType.value === 'line') {
        chartData.value = [{
          x: [1, 2, 3, 4],
          y: [10, 15, 13, 17],
          mode: 'lines'
        }];

        chartLayout.value = {
          title: 'Line Chart',
          height: 400,
          width: 500
        };
      }
    };
    const test = async () => {
      console.log("test");
      const system = "Always respond with JSON";
      const query = "TSLA's historical price from 2011 to 2020";
      const url = `http://localhost:8081/api/chat?system=${encodeURIComponent(system)}&query=${encodeURIComponent(query)}`;
  
      try {
        const response = await fetch(url);
        
        if (!response.ok) {
          throw new Error('Error fetching data');
        }
        
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error(error);
        throw error;
      }
    };

    return {
      chartType, chartData, chartLayout, test
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
