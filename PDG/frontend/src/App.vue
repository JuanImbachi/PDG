<template>
  <v-app>
    <toolbar></toolbar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Toolbar from './components/Toolbar';

export default {
  name: 'App',

  components: {
    Toolbar,
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
