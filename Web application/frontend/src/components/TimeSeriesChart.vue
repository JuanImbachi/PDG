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
  props: ["City","Neighborhoods"],
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
          text: "DATOS HISTÓRICOS"
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
       // In this Promise we will create our DataStore and using that we will create a custom DataTable which takes two
      // parameters, one is data another is schema.
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
        // First we are creating a DataStore
        const fusionDataStore = new FusionCharts.DataStore();
        // After that we are creating a DataTable by passing our data and schema as arguments
        const fusionTable = fusionDataStore.createDataTable(data, schema);
        // After that we simply mutated our timeseries datasource by attaching the above
        // DataTable into its data property.
        this.dataSource.data = fusionTable;
        //this.forceRerender()
        this.showChart = true
      } );
    }
  },

  watch: {
    Neighborhoods: function(newVal, oldVal) { // watch it
        this.generateChart()
    }
  },
};
</script>
