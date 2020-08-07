<template>
  <v-app>
    <div>
        <toolbar></toolbar>
          <router-view></router-view>
        </div>
      </div>
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
