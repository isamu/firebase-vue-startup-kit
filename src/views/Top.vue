<template>
  <div class="mx-3 my-1">
    <h2>Firebase vue Startup kit</h2>
    <div>
      <textarea v-model="query" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"></textarea>
    </div>
    <button v-on:click="askLLM" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">Ask</button>
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
      chartData, chartLayout, askLLM, query
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
