<template>
  <v-app class="mainContainer">
    <navbar :key="$route.fullPath" />

    <v-main class="grey lighten-5">
      <router-view ></router-view>
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
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;1,300;1,400&display=swap');
.mainContainer{
  font-family: 'Poppins', sans-serif;
}

</style>
