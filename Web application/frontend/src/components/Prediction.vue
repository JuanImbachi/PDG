<template>
  <div class="mx-16 mb-4">
    <v-container fluid>
      <v-row justify="space-around" dense class="ma-0">
        <v-col>
          <v-card>
            <v-col cols="12" >
              <div class="subtitle-2 grey--text">OPCIONES DE PREDICCIÓN</div>
            </v-col>
            <v-row justify="space-around" dense class="ml-2">
              <v-col>
              <v-select
                outlined
                dense
                :menu-props="{ top: false, offsetY: true }"
                v-model="selected_city"
                :items="cities"
                item-text="name"
                label="Ciudad"
                @change="citySelected"
                required
              />
            </v-col>
            <v-col>
              <v-select
                  outlined
                  dense
                  :menu-props="{ offsetY: true }"
                  v-model="selected_neighborhood"
                  :items="neighborhoods"
                  label="Barrio"
                  :loading="neighborhoods.length==0"
                  no-data-text="Cargando..."
                />
            </v-col>
            <v-col align="center">
              <v-btn outlined  medium color="primary" :width="'80%'" @click="getPrediction"> <v-icon left>mdi-cloud-search-outline</v-icon>PREDECIR</v-btn>
            </v-col>
            </v-row>

          </v-card>
        </v-col>
      </v-row>

      <v-card class="my-3">
        <v-row justify="space-around" align="center" dense class="ma-0">
          <v-col>
            <v-img :src="src" aspect-ratio="1.2" contain ></v-img>
          </v-col>

          <v-col>
            <map-component :mapCoords="mapCoords" :mapZoom="mapZoom"></map-component>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import MapGoogle from './Map';
import apiDengue from "@/apiDengue";
import swal from 'sweetalert'

export default {
   components: {
     mapComponent: MapGoogle,
   },
   data() {
     return {
      selected_city: "Buga",
      selected_neighborhood: "",
      neighborhoods: [],
      cities: [
              { name: 'Buga', position: {lat: 3.9, lng: -76.3}, zoom: 13.5},
              { name: 'Girón', position: {lat: 7.067, lng: -73.167}, zoom: 14},
              { name: 'Yopal', position: {lat: 5.3307, lng: -72.3951}, zoom: 13},
      ],
      mapCoords: {
        lat : 0,
        lng : 0
      },
      mapZoom : 0,
      src: require('../assets/download.png'),
     }
   },
   methods: {
     async getPrediction (){
      if(this.selected_neighborhood == ""){
         swal("Información incompleta", 'Seleccione al menos un barrio.', 'error')
       }else{
        var body = {
            city: this.selected_city,
            neighborhood: this.selected_neighborhood,
          }

          await apiDengue.getPrediction(JSON.stringify(body)).then((response) => {
              console.log(response)
          })
       }
     },

     citySelected (){
        this.getCityInfo()
        this.getNeighborhoods()
      },

      getCityInfo () {
        let cityInfo = this.cities.find(city => city.name === this.selected_city);
        this.mapCoords = cityInfo.position
        this.mapZoom = cityInfo.zoom;
     },

     getNeighborhoods (){
       this.neighborhoods = []
       this.selected_neighborhood= ""
       apiDengue.getNeighborhoodsToPredict(this.selected_city).
       then((response) => {
         this.neighborhoods = response.data.data
       })
     },

     getCityInfo () {
        let cityInfo = this.cities.find(city => city.name === this.selected_city);

        this.mapCoords = cityInfo.position

        this.mapZoom = cityInfo.zoom;
     },
   },
  computed: {
    allMonthsSelected () {
        return this.selected_months.length === this.months.length
      },
      someMonthsSelected () {
        return this.selected_months.length > 0 && !this.allMonthsSelected
      },
      iconMonth () {
        if (this.allMonthsSelected) return 'mdi-close-box'
        if (this.someMonthsSelected) return 'mdi-minus-box'
        return 'mdi-checkbox-blank-outline'
      }
  },

  created() {
    this.getCityInfo()
    this.getNeighborhoods()
  },
}
</script>

<style scoped>

</style>
