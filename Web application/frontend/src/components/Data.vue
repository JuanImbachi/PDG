<template>
  <div class="mx-16 mb-4">
    <v-container fluid>
      <v-card>
        <v-row justify="space-around" dense class="ma-0">
          <v-col class="ml-2" >
            <v-col>
              <div class="subtitle-2 grey--text ">Opciones de Filtrado</div>
            </v-col>
            <v-row justify="space-around" dense >
            <v-col >
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
            <v-col>
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
            <v-col >
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
            <v-col align="center">
              <v-btn outlined  medium color="primary" :width="'80%'" @click="filterData" > <v-icon left>mdi-cloud-search-outline</v-icon>FILTRAR</v-btn>
            </v-col>
          </v-row >
        </v-col>
      </v-row>
      </v-card>
      <v-card class="my-3">
        <v-row justify="space-around" align="center" >
          <v-col>
              <chart-component />
          </v-col>
        </v-row>
      </v-card>
      <v-card>
        <v-row justify="space-around" align="center">
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
import TimeSeriesChart from './TimeSeriesChart'
import apiDengue from "@/apiDengue";

export default {
  components: {
     mapComponent: MapGoogle,
     chartComponent :TimeSeriesChart,
  },
  data() {
    return {
      selected_city: "Buga",
      selected_years: [],
      selected_neighborhoods: [],
      cities: [
              { name: 'Buga', position: {lat: 3.9, lng: -76.3}, zoom: 13.5},
              { name: 'Girón', position: {lat: 7.067, lng: -73.167}, zoom: 14},
              { name: 'Yopal', position: {lat: 5.3307, lng: -72.3951}, zoom: 13},
      ],
      years: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
      neighborhoods: ['SANTA BARBARA', 'LA MERCED'],
      mapCoords: {
        lat : 0,
        lng : 0
      },
      cases: [],
      mapZoom : 0,
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
        var body = {
          city: this.selected_city,
          years: this.selected_years,
          neighborhoods: this.selected_neighborhoods
        }

        apiDengue.getCasesByCity(JSON.stringify(body))
        .then((response) => {
          var general_data= JSON.parse(response.data.data)

          general_data.forEach(element => {
            this.cases.push(element.fields)
          });
        })
      },

      getCityInfo () {
        let cityInfo = this.cities.find(city => city.name === this.selected_city);

        this.mapCoords = cityInfo.position

        this.mapZoom = cityInfo.zoom;
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
          if (this.allCeighborhoodsSelected) {
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
