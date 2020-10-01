<template>
  <v-app>
    <navbar />

    <v-main>
      <router-view></router-view>
    </v-main>

    <v-footer  padless>
      <v-card class="flex" flat tile>
        <v-card-text class="py-2  text-center">
            {{ new Date().getFullYear() }} — <strong>Universidad Icesi</strong>
          </v-card-text>
        </v-card>
    </v-footer>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar';
import Footer from './components/Footer'
export default {
  name: 'App',

  components: {
    Navbar,
    Footer
  },

  data: () => ({
    //
  }),
};
</script>

<style>

</style>
