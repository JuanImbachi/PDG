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
                required
              />
            </v-col>
            <v-col>
              <v-select
                outlined
                dense
                :menu-props="{ top: false, offsetY: true }"
                v-model="selected_numberMonths"
                :items="months"
                label="Meses a futuro"
                required
              />
            </v-col>
            <v-col align="center">
              <v-btn outlined  medium color="primary" :width="'80%'" @click="getPrediction"> <v-icon left>mdi-cloud-search-outline</v-icon>PREDECIR</v-btn>
            </v-col>
            </v-row>

          </v-card>
        </v-col>

        <v-col>
          <v-card>
              <v-col cols="12" >
                <div class="subtitle-2 grey--text">OPCIONES DE FILTRADO</div>
              </v-col>
              <v-row justify="space-around" dense class="ml-2">
                <v-col>
                  <v-select
                      outlined
                      dense
                      :menu-props="{ offsetY: true }"
                      v-model="selected_communes"
                      :items="communes"
                      label="Comuna"
                      multiple
                    >
                    <template v-slot:prepend-item>
                        <v-list-item
                          @click="allCommunes"
                        >
                        <v-list-item-action>
                          <v-icon :color="selected_communes.length > 0 ? 'light-blue darken-2' : ''">
                            {{ iconCommune }}
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
                              (+{{ selected_communes.length - 1 }})
                            </span>
                      </template>
                    </v-select>
                  </v-col>

                  <v-col>
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
                  <v-btn outlined  medium color="primary" :width="'80%'" @click="filterData"> <v-icon left>mdi-cloud-search-outline</v-icon>FILTRAR</v-btn>
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

export default {
   components: {
     mapComponent: MapGoogle,
   },
   data() {
     return {
      selected_city: "Buga",
      selected_numberMonths: [],
      selected_communes: [],
      selected_neighborhoods: [],
      months: ['1', '2', '3'],
      communes: ['Comuna 1', 'Comuna 2', 'Comuna 3'],
      neighborhoods: ['Barrio 1', 'Barrio 2', 'Barrio 3'],
      cities: [
              { name: 'Buga', position: {lat: 3.9, lng: -76.3}, zoom: 13.5},
              { name: 'Cali', position: {lat: 3.42158, lng: -76.5205}, zoom: 12},
              { name: 'Girón', position: {lat: 7.067, lng: -73.167}, zoom: 14},
              { name: 'Palmira', position: {lat: 3.5307, lng: -76.2961}, zoom: 13},
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
     filterData (){

     },
     getPrediction () {
       this.getCityInfo()
     },
     getCityInfo () {
        let cityInfo = this.cities.find(city => city.name === this.selected_city);

        this.mapCoords = cityInfo.position

        this.mapZoom = cityInfo.zoom;
     },
      allCommunes () {
        this.$nextTick(() => {
          if (this.allCommunesSelected) {
            this.selected_communes = []
          } else {
            this.selected_communes = this.communes.slice()
          }
        })
      },
      allNeighborhoods() {
        this.$nextTick(() => {
          if (this.allNeighborhoodsSelected) {
            this.selected_neighborhoods = []
          } else {
            this.selected_neighborhoods = this.neighborhoods.slice()
          }
        })
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
      },
      allCommunesSelected () {
        return this.selected_communes.length === this.communes.length
      },
      someCommunesSelected () {
        return this.selected_communes.length > 0 && !this.allCommunesSelected
      },
      iconCommune () {
        if (this.allCommunesSelected) return 'mdi-close-box'
        if (this.someCommunesSelected) return 'mdi-minus-box'
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

<style scoped>

</style>
