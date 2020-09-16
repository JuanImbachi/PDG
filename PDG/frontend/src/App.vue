<template>
  <v-app>
    <div>
        <appbar></appbar>
        <router-view></router-view>
        <v-footer
          absolute
          padless
          dark
        >
          <v-col
            class="text-center"
            cols="12"
          >
            {{ new Date().getFullYear() }} — <strong>Icesi</strong>
          </v-col>
        </v-footer>
    </div>
  </v-app>
</template>

<script>
import Appbar from './components/Appbar';
import Footer from './components/Footer'
export default {
  name: 'App',

  components: {
    Appbar,
    Footer
  },

  data: () => ({
    //
  }),
};
</script>

<style>

  .v-application--wrap{
    background-attachment: fixed;
    background-position: center center;
    background-size: cover;
    background-image: url("assets/bg.jpg");
  }
</style>
