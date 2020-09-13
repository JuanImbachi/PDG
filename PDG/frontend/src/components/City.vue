<template>
  <v-container class="grey lighten-5">
    <v-row class="pa-5">
      <h1>Welcome to {{ getRouteId() }}</h1>

      <v-spacer></v-spacer>

      <v-btn class="mt-2" outlined color="primary">
        <v-icon left>mdi-cog</v-icon>
        Settings
      </v-btn>
    </v-row>

    <v-container class="grey lighten-2 mb-6 ">
      <v-row
        no-gutters
        style="height: 150px;"
        align="center"
        justify="center"
      >
        <v-col class="pa-2">
          <v-card
            class="pa-2 text-center"
            outlined
            tile
          >
            Timeline
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <map-component></map-component>
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
       src: require('../assets/Palmira.png'),
     }
   },
   methods: {
     getRouteId(){
       this.id = this.$route.params.id
       return this.id;
     }
   },

}
</script>

<style>

</style>
