<template>
    <v-app-bar app class="blue-grey darken-3" >
        <v-toolbar-title>
          <router-link tag="span" to="/" style="cursor:pointer" class="white--text">Seguimiento de Casos de Dengue</router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn  to="/predictions" class="white--text" text dense> Predicciones </v-btn>
        <v-btn class="mx-2 white--text" to="/data" text color > Datos </v-btn>
        <v-btn class="pa-4 white--text" to="/login" outlined > Iniciar Sesión <v-icon right >mdi-account-lock</v-icon> </v-btn>
    </v-app-bar>
</template>


<script>
export default {
  name: "Navbar",
  data() {
    return{
    }
  }
}
</script>

<style>

</style>
