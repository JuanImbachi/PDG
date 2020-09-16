<template>
  <v-container>
      <v-carousel hide-delimiters>
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        style="width: auto;height:auto;"
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
            src: require('../assets/4.png'),
          },
          {
            src: require('../assets/5.png'),
          },
        ],
      }
    },
  }
</script>

<style>


</style>
