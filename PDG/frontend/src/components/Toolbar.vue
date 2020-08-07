<template>
<div>
  <v-toolbar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>SGTCD - Palmira</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="mx-2"> Sign In </v-btn>
      <v-btn class="mx-2" color="primary"> Sign Up </v-btn>

    </v-toolbar>
    <v-navigation-drawer app v-model="drawer" temporary dark>
      <v-layout mt-4 column align-center>
        <h3 class="white--text headline">Vertical Menu</h3>
        <v-flex><p class="white--text mt-3 headline">Comuna 1</p> </v-flex>
        <v-flex><p class="white--text mt-3 headline">Comuna 2</p> </v-flex>
        <v-flex><p class="white--text mt-3 headline">Comuna 3</p> </v-flex>
        <v-flex><p class="white--text mt-3 headline">Comuna 4</p> </v-flex>
        <v-flex><p class="white--text mt-3 headline">Comuna 5</p> </v-flex>
        <v-flex><p class="white--text mt-3 headline">Comuna 6</p> </v-flex>
        <v-flex><p class="white--text mt-3 headline">Comuna 7</p> </v-flex>
        <v-flex><p class="white--text mt-3 headline">Comuna 8</p> </v-flex>
      </v-layout>
    </v-navigation-drawer>
</div>

</template>


<script>
export default {
  name: "Toolbar",
  data() {
    return{
      drawer: false
    }
  }
}
</script>

<style>

</style>
