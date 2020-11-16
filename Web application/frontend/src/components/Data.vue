<template>
  <div class="mx-16 mb-4">
    <v-container fluid>
      <v-row >
        <v-col align="start">
          <div class="subtitle-2 grey--text ">Opciones de Filtrado</div>
        </v-col>
      </v-row>
      <v-row justify="start" dense >
        <v-col cols="2">
          <v-select
            outlined
            dense
            :menu-props="{ top: false, offsetY: true }"
            v-model="selected_city"
            :items="cities"
            item-text="name"
            label="Ciudad"
            required
            @change="citySelected"
          ></v-select>
        </v-col>
        <v-col cols="2" >
          <v-select
              outlined
              dense
              :menu-props="{ offsetY: true }"
              v-model="selected_neighborhoods"
              :items="neighborhoods"
              label="Barrio"
              multiple
            >
            <template v-slot:prepend-item>
                <v-list-item
                  @click="allNeighborhoods"
                >
                <v-list-item-action>
                  <v-icon :color="selected_neighborhoods.length > 0 ? 'light-blue darken-2' : ''">
                    {{ iconNeighborhood }}
                  </v-icon>
                </v-list-item-action>
                  <v-list-item-content>
                    <v-list-item-title>
                      Selecccionar Todo
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-divider class="mt-2"></v-divider>
              </template>
              <template v-slot:selection="{ item, index }">
                    <div class="mr-2" v-if="index === 0">
                      <span>{{ item }}</span>
                    </div>
                    <span
                      v-if="index === 1"
                      class="grey--text caption"
                    >
                      (+{{ selected_neighborhoods.length - 1 }})
                    </span>
              </template>
          </v-select>
        </v-col>
        <v-col align="center" cols="1">
          <v-btn outlined  color="primary" @click="filterData" >
            <v-icon left>mdi-cloud-search-outline</v-icon>FILTRAR
          </v-btn>
        </v-col>
      </v-row >

      <v-card class="my-3">
        <v-row justify="space-around" align="center" >
          <v-col>
              <chart-component  :City="city_to_search" :Neighborhoods="neighborhoods_to_search" :isPrediction="false" />
          </v-col>
        </v-row>
      </v-card>
      <v-card >
        <v-row justify="space-between">
          <v-col cols="2" class=" mb-n6 ml-2">
            <v-select
                outlined
                dense
                :menu-props="{ offsetY: true }"
                v-model="selected_years"
                :items="years"
                label="Año"
                multiple
                @change="yearSelected"
              >
              <template v-slot:prepend-item>
                <v-list-item
                  @click="allYears"
                >
                <v-list-item-action>
                  <v-icon :color="selected_years.length > 0 ? 'light-blue darken-2' : ''">
                    {{ iconYear }}
                  </v-icon>
                </v-list-item-action>
                  <v-list-item-content>
                    <v-list-item-title>
                      Selecccionar Todo
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-divider class="mt-2"></v-divider>
              </template>
              <template v-slot:selection="{ item, index }">
                <div class="mr-2" v-if="index === 0">
                  <span>{{ item }}</span>
                </div>

                <span
                  v-if="index === 1"
                  class="grey--text caption"
                >
                  (+{{ selected_years.length - 1 }})
                </span>
              </template>
            </v-select>
          </v-col>
          <v-col>
            <v-btn fab small outlined  color="primary" @click="getMapData" >
              <v-icon icon >mdi-magnify</v-icon>
            </v-btn>
          </v-col>
        </v-row>
        <v-row justify='center'>
          <map-component :mapCoords="mapCoords" :mapZoom="mapZoom" :mapPoints="mapPoints"></map-component>
          <small class="mb-2">Ubicación sujeta al API de Google Maps</small>
        </v-row> 
      </v-card>
    </v-container>
  </div>
</template>

<script>
import MapGoogle from './Map';
import TimeSeriesChart from './TimeSeriesChart'
import apiDengue from "@/apiDengue";
import swal from 'sweetalert'

export default {
  components: {
     mapComponent: MapGoogle,
     chartComponent :TimeSeriesChart,
  },
  data() {
    return {
      selected_city: "Buga",
      city_to_search: "",
      selected_years: [],
      selected_neighborhoods: [],
      neighborhoods_to_search: [],
      cities: [
              { name: 'Buga', position: {lat: 3.9, lng: -76.3}, zoom: 13.5},
              { name: 'Girón', position: {lat: 7.067, lng: -73.167}, zoom: 14},
              { name: 'Yopal', position: {lat: 5.3307, lng: -72.3951}, zoom: 13},
      ],
      years: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
      neighborhoods: [],
      mapCoords: {
        lat : 0,
        lng : 0
      },
      mapZoom : 0,
      mapPoints : [],
      src: require('../assets/download.png'),
    }
  },

    methods: {
      citySelected (){
        this.disabled_years = false
        this.getCityInfo()
        this.getNeighborhoodsByCity()
      },

      yearSelected (){
        this.disabled_neighborhoods = false
      },

      filterData () {
        if(this.selected_neighborhoods.length == 0){
          swal("Seleccione al menos un barrio", '', 'error')
        }else{
          this.city_to_search = this.selected_city
          this.neighborhoods_to_search = this.selected_neighborhoods
        }
      },

      getCityInfo () {
        let cityInfo = this.cities.find(city => city.name === this.selected_city);
        this.mapCoords = cityInfo.position
        this.mapZoom = cityInfo.zoom;
     },

     async getMapData(){
       if(this.neighborhoods_to_search.length == 0 || this.selected_years.length == 0){
         swal("Información incompleta", 'Seleccione al menos un barrio y un año.', 'error')
       }else{
        var errorMessage = ''
        var body = {
            city: this.city_to_search,
            neighborhoods: this.neighborhoods_to_search,
            years: this.selected_years
          }
          var neighborhoodsCount = []
          var points = []
          await apiDengue.getCasesCountByCityNeighborhoodYear(JSON.stringify(body))
          .then((response) => {
            neighborhoodsCount = response.data.data
          })

          neighborhoodsCount.forEach(element => {
            var location = {}
            var viewport = {}
            var auxCity = ""
            if(this.city_to_search === 'Buga') {
              auxCity = 'Guadalajara de Buga'
            }else{
              auxCity = this.city_to_search
            }
            apiDengue.getLocation(auxCity, element[0]).then((response) => {
              try{
                location = response.data.results[0].geometry.location
                viewport = response.data.results[0].geometry.viewport

                for(var i=0; i< element[1]; i++){
                  var latVal = Math.random()*(viewport.northeast.lat-viewport.southwest.lat) + location.lat
                  var lngVal = Math.random()*(viewport.northeast.lng-viewport.southwest.lng) + location.lng
                  var newPoint = {lat:latVal, lng:lngVal}
                  points.push(newPoint)
                }
              }catch(err){
                 errorMessage += element[0]+", "
                 swal("Barrios no encontrados:",errorMessage, 'error')
              }
            })

          });

          this.mapPoints = points

       }
     },

     getNeighborhoodsByCity (){
       apiDengue.getNeighborhoodsByCity(this.selected_city)
       .then((response) => {
         this.neighborhoods = response.data.data
       })
     },

     allYears () {
        this.$nextTick(() => {
          if (this.allYearsSelected) {
            this.selected_years = []
          } else {
            this.selected_years = this.years.slice()
          }
        })
      },

      allNeighborhoods () {
        this.$nextTick(() => {
          if (this.allNeighborhoodsSelected) {
            this.selected_neighborhoods = []
          } else {
            this.selected_neighborhoods = this.neighborhoods.slice()
          }
        })
      },

    },
    created() {
      this.getCityInfo()
      this.getNeighborhoodsByCity()
    },

    watch: {
      selected_city(){
        this.selected_neighborhoods= []
      }
    },

    computed: {
      allYearsSelected () {
        return this.selected_years.length === this.years.length
      },
      someYearsSelected () {
        return this.selected_years.length > 0 && !this.allYearsSelected
      },
      iconYear () {
        if (this.allYearsSelected) return 'mdi-close-box'
        if (this.someYearsSelected) return 'mdi-minus-box'
        return 'mdi-checkbox-blank-outline'
      },

      allNeighborhoodsSelected () {
        return this.selected_neighborhoods.length === this.neighborhoods.length
      },
      someNeighborhoodsSelected () {
        return this.selected_neighborhoods.length > 0 && !this.allNeighborhoodsSelected
      },
      iconNeighborhood () {
        if (this.allNeighborhoodsSelected) return 'mdi-close-box'
        if (this.someNeighborhoodsSelected) return 'mdi-minus-box'
        return 'mdi-checkbox-blank-outline'
      },
    },


}
</script>

<style>

</style>
