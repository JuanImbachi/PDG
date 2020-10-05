<template>
  <v-container>
      <vue-google-heatmap
        :points="points"
        :height="450"
        :lat="myCoordinates.lat"
        :lng="myCoordinates.lng"
        :initial-zoom="zoomCt"
        :key="mapKey"
      />
  </v-container>

</template>

<script>
    export default {
      props: ["mapCoords", "mapZoom"],
      data(){
        return {
          mapKey: 0,
          myCoordinates: {
              lat: 0,
              lng: 0
          },
          zoomCt: 13,
          points: [
            {lat: 37.786117, lng:-122.440119},
            {lat: 37.786564, lng:-122.440209},
            {lat: 37.786905, lng:-122.440270},
            {lat: 37.786956, lng:-122.440279},
            {lat: 37.800224, lng:-122.433520},
            {lat: 37.800155, lng:-122.434101},
            {lat: 37.800160, lng:-122.434430},
            {lat: 37.800378, lng:-122.434527},
            {lat: 37.800738, lng:-122.434598},
            {lat: 37.800938, lng:-122.434650},
            {lat: 37.801024, lng:-122.434889},
            {lat: 37.800955, lng:-122.435392},
            {lat: 37.800886, lng:-122.435959}
          ]
        }
        },
        methods: {
          forceRerender() {
            this.mapKey += 1;
          }
        },
        mounted(){
          this.myCoordinates = this.mapCoords;
          this.zoomCt = this.mapZoom;
        },
        watch:{
          mapCoords(){
            this.myCoordinates = this.mapCoords;
            this.forceRerender()
          },
          mapZoom () {
            this.zoomCt = this.mapZoom;
          }
        }
    }
</script>

<style scoped>

</style>
