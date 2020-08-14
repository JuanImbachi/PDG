<template>
  <v-container>
      <v-carousel height="auto" >
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
      ></v-carousel-item>
    </v-carousel>
  </v-container>
</template>

<script>
export default {
    data () {
      return {
        items: [
          {
            src: require('../assets/1.png'),
          },
          {
            src: require('../assets/2.png'),
          },
          {
            src: require('../assets/3.png'),
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
          },
        ],
      }
    },
  }
</script>

<style>

.container {
    margin-top : 4%;
}

</style>
