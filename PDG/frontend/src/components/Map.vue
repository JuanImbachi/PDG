<template>
    <div>
        <div style="display: flex; align-items: center; justify-content: space-between">
            <div class="left">
                <h1>Your coordinates:</h1>
                <p>{{myCoordinates.lat}} Latitude, {{myCoordinates.lng}} Longitude</p>
            </div>
            <div class="right">
                <h1>Map coordinates:</h1>
                <p>{{mapCoordinates.lat}} Latitude, {{mapCoordinates.lng}} Longitude</p>
            </div>
        </div>
        <google-map
            :center="myCoordinates"
            :zoom="13"
            style="width:640px; height:360px; margin: 32px auto;"
            ref="mapRef"
        ></google-map>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                map: null,
                myCoordinates: {
                    lat: 0,
                    lng: 0
                }
            }
        },
        created() {
            this.$getLocation({})
                .then(coordinates => {
                    this.myCoordinates = coordinates;
                })
                .catch(error => alert(error));
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