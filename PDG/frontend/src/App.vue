<template>
  <v-app>
    <div>
        <appbar></appbar>
        <!-- <router-view></router-view> -->
        <Map/>
    </div>
  </v-app>
</template>

<script>
import Appbar from './components/Appbar';
import Map from './components/Map';

export default {
  name: 'App',

  components: {
    Appbar, Map
  },

  data: () => ({
    //
  }),
};
</script>

<style>

  .container{
    background-color: gray;
  }
</style>
