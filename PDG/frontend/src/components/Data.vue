<template>
<div class="mx-16 mb-4">
  <v-container fluid>
      <v-row justify="space-around" dense class="ma-0">
        <v-col cols="12" >
          <div class="subtitle-2 grey--text">OPCIONES DE FILTRADO</div>
        </v-col>
        <v-col>
          <v-select
            outlined
            dense
            :menu-props="{ top: false, offsetY: true }"
            v-model="selected_city"
            :items="cities"
            label="Ciudad"
            required
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
        <v-select
            outlined
            dense
            :menu-props="{ offsetY: true }"
            v-model="selected_months"
            :items="months"
            label="Mes"
            multiple
          >
          <template v-slot:prepend-item>
              <v-list-item
                @click="allMonths"
              >
              <v-list-item-action>
                <v-icon :color="selected_months.length > 0 ? 'light-blue darken-2' : ''">
                  {{ iconMonth }}
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
                    (+{{ selected_months.length - 1 }})
                  </span>
            </template>
          </v-select>
        </v-col>

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
          <v-btn outlined  medium color="primary" :width="'80%'" > <v-icon left>mdi-cloud-search-outline</v-icon>FILTRAR</v-btn>
        </v-col>
      </v-row>

      <v-card class="my-3">
          <v-row justify="space-around" align="center" dense class="ma-0">
              <v-col>
                  <v-img :src="src" aspect-ratio="1.2" contain ></v-img>
              </v-col>

              <v-col>
                <map-component :coordinates="coords" :cityZoom="cz"></map-component>
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
      selected_city: "",
      selected_years: [],
      selected_months: [],
      selected_communes: [],
      selected_neighborhoods: [],
      months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
      cities: ['Buga', 'Cali', 'Palmira', 'Yopal', 'Girón' ],
      years: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
      communes: ['Comuna 1', 'Comuna 2', 'Comuna 3'],
      neighborhoods: ['Barrio 1', 'Barrio 2', 'Barrio 3'],
      coords: {
        lat : 0,
        lng : 0
      },
      cz : 0,
      src: require('../assets/download.png'),
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

    methods: {
      allYears () {
        this.$nextTick(() => {
          if (this.allYearsSelected) {
            this.selected_years = []
          } else {
            this.selected_years = this.years.slice()
          }
        })
      },
      allMonths () {
        this.$nextTick(() => {
          if (this.allMonthsSelected) {
            this.selected_months = []
          } else {
            this.selected_months = this.months.slice()
          }
        })
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
}
</script>

<style>

</style>
