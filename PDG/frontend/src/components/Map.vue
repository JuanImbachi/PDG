<template>
    <v-container>
        <google-map
            :center="myCoordinates"
            :zoom="zoomCt"
            style="width:auto; height:25em; margin: 32px auto; border: white 3px inset;"
            ref="mapRef"
        ></google-map>
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
                zoomCt: 13
            }
        },
        created() {

          this.myCoordinates = this.coordinates;
          this.zoomCt = this.cityZoom;

        },
        mounted() {

            this.$refs.mapRef.$mapPromise.then(map => this.map = map);
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

<style>
    .left {
        margin-left: 10%;
        text-align:center;
    }
    .right {
        margin-right: 10%;
        text-align:center;

    }
</style>
