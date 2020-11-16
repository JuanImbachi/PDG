<template>
<div class="text-center" >
  <span v-if="Neighborhoods==''">Seleccione los barrios a mostrar</span>
    <v-progress-circular
      :size="80"
      color="primary"
      indeterminate
      v-else-if="!showChart"
    ></v-progress-circular>
    <fusioncharts
    :type="type"
    :width="width"
    :height="height"
    :dataFormat="dataFormat"
    :dataSource="dataSource"
    v-if="showChart"
  ></fusioncharts>
</div>


</template>

<script>
import Vue from "vue";
import VueFusionCharts from "vue-fusioncharts";
import FusionCharts from "fusioncharts";
import TimeSeries from "fusioncharts/fusioncharts.timeseries";
import apiDengue from "@/apiDengue";

Vue.use(VueFusionCharts, FusionCharts, TimeSeries);

export default {
  props: ["City","Neighborhoods", "isPrediction"],
  name: "FChart",
  data() {
    return {
      showChart: false,
      type: "timeseries",
      width: "100%",
      height: "500",
      dataFormat: "json",
      dataSource: {
        chart:{
          theme: 'candy'
        },
        data: null,
        caption: {
          text: ""
        },
        subcaption: {
          text: "Dengue"
        },
        series: "Type",
        yAxis: [
          {
            allowDecimals: false,
            plot: "Cases",
            title: "Número de Casos Reportados",
          }
        ]
      }
    };
  },
  methods: {

    generateChart () {
      this.showChart = false

      if(this.isPrediction) {
        apiDengue.getPrediction(JSON.stringify({city: this.City, neighborhood: this.Neighborhoods})).then((response) =>{
          var data = response.data.data[0]

          this.$emit('update-map',response.data.data[1])
          
          const schema = [{
            "name": "Time",
            "type": "date",
            "format": "%Y-%m-%d"
          },
          {
            "name": "Type",
            "type": "string"
          },
          {
            "name": "Cases",
            "type": "number"
          }]
          
          const fusionDataStore = new FusionCharts.DataStore();
          const fusionTable = fusionDataStore.createDataTable(data, schema); 
          this.dataSource.data = fusionTable;
          this.dataSource.caption.text = "PREDICCIONES"
          this.showChart = true
        } );
      }else {
        apiDengue.getCasesByCityNeighborhood(JSON.stringify({city: this.City, neighborhood: this.Neighborhoods})).then((response) =>{
          
          var data = response.data.data
          const schema = [{
            "name": "Time",
            "type": "date",
            "format": "%Y-%m-%d"
          },
          {
            "name": "Type",
            "type": "string"
          },
          {
            "name": "Cases",
            "type": "number"
          }]
          
          const fusionDataStore = new FusionCharts.DataStore();
          const fusionTable = fusionDataStore.createDataTable(data, schema); 
          this.dataSource.data = fusionTable;
          this.dataSource.caption.text = "DATOS HISTÓRICOS"
          this.showChart = true
        } );
      }
      
    }
  },

  watch: {
    Neighborhoods: function(newVal, oldVal) { // watch it
        this.generateChart()
    }
  },
};
</script>
