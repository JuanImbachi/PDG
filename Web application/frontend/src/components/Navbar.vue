<template>
    <v-app-bar app class="blue-grey darken-3" >
        <v-toolbar-title>
          <router-link tag="span" to="/" style="cursor:pointer" class="white--text">Seguimiento de Casos de Dengue</router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn  to="/predictions" class="white--text" text dense> Predicciones </v-btn>
        <v-btn class="mx-2 white--text" to="/data" text> Datos </v-btn>
        <v-btn class="mx-2 white--text" to="/registers" text v-if="token!=null"> Registros </v-btn>
        <v-btn class=" red pa-4 white--text" outlined @click="logout" v-if="token!=null"> Cerrar Sesión <v-icon right>mdi-logout</v-icon> </v-btn>
        <v-btn class="pa-4 white--text" to="/login" outlined v-if="token==null"> Iniciar Sesión <v-icon right >mdi-account-lock</v-icon> </v-btn>
    </v-app-bar>
</template>


<script>
export default {
  name: "Navbar",
  data() {
    return{
      token: localStorage.getItem('user-token') || null,
    }
  },
  methods: {
    logout (){
      localStorage.removeItem('user-token')
      this.$router.push('/')
      this.token = null
    }
  },
}
</script>

<style>

</style>
