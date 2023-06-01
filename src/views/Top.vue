<template>
  <div>
    <h2>Firebase vue Startup kit</h2>
    <p>{{ query }}</p>
    <button v-on:click="askLLM">Ask</button>
    <div class="chart-container">
      <Plotly v-if="chartData" :data="chartData" :layout="chartLayout" :display-mode-bar="false" />
    </div>
  </div>
</template>

<script>
import { Plotly } from 'vue-plotly';
import { ref } from 'vue';

export default {
  components: {
    Plotly,
  },
  name: 'Top',
  setup() {
    const chartType = ref('');
    const chartData = ref(null);
    const chartLayout = ref({});
    const query = ref('The historical GDP of United states form 2011 to 2020');
    const system = "Respond as an list of objects with attributes 'label' and 'value' in JSON format. Always respond only in JSON without any words around it";

    const askLLM = async () => {
      chartData.value = null;
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
