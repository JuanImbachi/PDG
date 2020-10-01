<template>
  <v-container>
      <vue-google-heatmap :points="points" :height="450" />
  </v-container>

</template>

<script>
    export default {
      props: ["coordinates", "cityZoom"],
        data(){
            return {
                map: null,
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
        created() {

          this.myCoordinates = this.coordinates;
          this.zoomCt = this.cityZoom;

        },

        computed: {
            mapCoordinates() {
                if(!this.map) {
                    return {
                        lat: 0,
                        lng: 0
                    };
                }
                return {
                    lat: this.map.getCenter().lat().toFixed(4),
                    lng: this.map.getCenter().lng().toFixed(4)
                }
            }
        },
        watch:{
          coordinates(){
            this.myCoordinates = this.coordinates;
            this.zoomCt = this.cityZoom;
          }
        }
    }
</script>

<style scoped>
html, body, .container,  #map {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
}
#map {
    position: relative;
}
</style>
