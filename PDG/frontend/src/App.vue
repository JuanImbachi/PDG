<template>
  <v-app>
    <div>
        <appbar></appbar>
        <router-view></router-view>
    </div>
  </v-app>
</template>

<script>
import Appbar from './components/Appbar';

export default {
  name: 'App',

  components: {
    Appbar,
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
