<template>
  <v-container>
    <v-row class="pa-1">
      <v-col cols="1">
        <v-btn class="mt-2" outlined color="black" @click="modal=!modal">
                <v-icon left>mdi-cog</v-icon>
                Opciones
        </v-btn>
      </v-col>
      <v-col align="center" cols="11">
       <h1 alig>  {{ id }}</h1>
      </v-col>
    </v-row>

    <v-dialog
      ref="dialog"
      v-model="modal"
      height="35%"
      width="35%"
    >
      <v-card>
        <v-card-title>
          <h1 class="headline"> Opciones de Predicción</h1>
        </v-card-title>
        <v-card-text>
          <v-container>

            <h4>¡Disponible en la siguiente versión de la aplicación!</h4>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="black" outlined @click="modal = false">Cerrar</v-btn>
          <v-btn color="black" outlined @click="modal = false">Guardar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

      <v-row
        no-gutters
        align="center"
        justify="center"
        class="blue-grey lighten-5 my-6 rounded-lg "
      >
        <v-col cols="7"  class="mr-1">
        <div >
          <v-img :src="src" aspect-ratio="1.2" contain ></v-img>
        </div>
        </v-col>
        <v-col cols="4" >
          <map-component :coordinates="coords" :cityZoom="cz"></map-component>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import MapGoogle from './Map';

export default {
   components: {
     mapComponent: MapGoogle,
   },
   data() {
     return {
       id: "",
       cities: [
              { title: 'Buga', position: {lat: 3.9, lng: -76.3}, zoom: 13.5},
              { title: 'Cali', position: {lat: 3.42158, lng: -76.5205}, zoom: 12},
              { title: 'Girón', position: {lat: 7.067, lng: -73.167}, zoom: 14},
              { title: 'Palmira', position: {lat: 3.5307, lng: -76.2961}, zoom: 13},
              { title: 'Yopal', position: {lat: 5.3307, lng: -72.3951}, zoom: 13},
            ],
      coords: {
        lat : 0,
        lng : 0
      },
      cz : 0,
      modal : false,
      src: require('../assets/download.png'),
     }
   },
   methods: {
     getRouteId(){
       this.id = this.$route.params.id
     },
     getCoordinates(){
        let cityInfo = this.cities.find(city => city.title === this.id);

        this.coords = cityInfo.position

        this.cz = cityInfo.zoom;
     },
     getInfo(){
       this.getRouteId()
       this.getCoordinates()
     }
   },
  mounted() {
    this.getInfo()
  },
  watch: {
  '$route'(to, from) {
    this.getInfo()
  }
},

}
</script>

<style scoped>

</style>
