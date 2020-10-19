<template>
    <v-app-bar app dark dense>
        <v-toolbar-title>
          <router-link tag="span" to="/" style="cursor:pointer">Seguimiento de Casos de Dengue</router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn  to="/predictions"  medium text dense> Predicciones </v-btn>
        <v-btn class="mx-2" to="/data"  medium text color > Datos </v-btn>
        <v-btn class="pa-4" to="/login"  small outlined > Iniciar Sesión <v-icon right >mdi-account-lock</v-icon> </v-btn>
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
