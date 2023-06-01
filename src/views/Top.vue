<template>
  <div>
    <h2>Firebase vue Startup kit</h2>
    <p>{{ query }}</p>
    <button v-on:click="askLLM">Ask</button>
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
    const query = ref('The historical GDP of United states form 2011 to 2020');
    const system = "Respond as an list of objects with attributes 'label' and 'value' in JSON format. Always respond only in JSON without any words around it";

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
    const askLLM = async () => {
      console.log("fetching...");
      const url = `http://localhost:8081/api/chat?system=${encodeURIComponent(system)}&query=${encodeURIComponent(query.value)}`;
  
      try {
        const response = await fetch(url);
        
        if (!response.ok) {
          throw new Error('Error fetching data');
        }
        
        const data = await response.json();
        console.log(data);
        const items = JSON.parse(data)
        chartData.value = [{
          x: items.map(item => item.label),
          y: items.map(item => item.value),
          type: 'bar'
        }];

        chartLayout.value = {
          title: query.value,
          width: 500,
          height: 500
        };
      } catch (error) {
        console.error(error);
        throw error;
      }
    };

    return {
      chartType, chartData, chartLayout, askLLM, query
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
