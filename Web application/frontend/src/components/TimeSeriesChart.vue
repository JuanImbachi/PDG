<template>
  <fusioncharts
    :type="type"
    :width="width"
    :height="height"
    :dataFormat="dataFormat"
    :dataSource="dataSource"
  ></fusioncharts>
</template>

<script>
import Vue from "vue";
import VueFusionCharts from "vue-fusioncharts";
import FusionCharts from "fusioncharts";
import TimeSeries from "fusioncharts/fusioncharts.timeseries";
import apiDengue from "@/apiDengue";

Vue.use(VueFusionCharts, FusionCharts, TimeSeries);



export default {
  name: "FChart",
  data() {
    return {
      type: "timeseries",
      width: "100%",
      height: "500",
      dataFormat: "json",
      dataSource: {
        data: null,
        caption: {
          text: "DATOS HISTÓRICOS"
        },
        subcaption: {
          text: "Dengue"
        },
        yAxis: [
          {
            plot: {
              value: "Number of Cases",
              type: "line"
            },
            format: {
              prefix: ""
            },
            title: "Número de Casos Reportados"
          }
        ]
      }
    };
  },
  mounted: function() {
    // In this Promise we will create our DataStore and using that we will create a custom DataTable which takes two
    // parameters, one is data another is schema.
    apiDengue.getCasesByCityNeighborhood(JSON.stringify({city:'Buga', neighborhood:'SANTA BARBARA'})).then((response) =>{

      const data = response.data.data
      const schema = [{
        "name": "Time",
        "type": "date",
        "format": "%y-%b-%d"
      }, {
        "name": "Number of Cases",
        "type": "number"
      }]
      // First we are creating a DataStore
      const fusionDataStore = new FusionCharts.DataStore();
      // After that we are creating a DataTable by passing our data and schema as arguments
      const fusionTable = fusionDataStore.createDataTable(data, schema);
      // After that we simply mutated our timeseries datasource by attaching the above
      // DataTable into its data property.
      this.dataSource.data = fusionTable;
    } );

  }
};
</script>
