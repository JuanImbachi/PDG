<template>
      <v-container class="mt-16">
        <v-row
          justify="center"
        >
          <v-col
            sm="8"
            md="4"
          >
            <v-card class="elevation-12 transparent">
              <v-toolbar
                class="blue-grey lighten-1 white--text"
                flat
              >
                <v-toolbar-title>Iniciar Sesión</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form ref="form" v-model="valid" >
                  <v-text-field
                      label="E-mail"
                      prepend-icon="mdi-account"
                      type="text"
                      v-model="email"
                      required
                      :rules="emailRules"
                  ></v-text-field>

                  <v-text-field
                      label="Contraseña"
                      v-model="password"
                      :append-icon="showpassword ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="showpassword ? 'text' : 'password'"
                      @click:append="showpassword = !showpassword"
                      prepend-icon="mdi-lock"
                      required
                      :rules="[v => (v!=='') || 'Contraseña requerida']"
                  ></v-text-field>
                  </v-form>
                </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="transparent" @click="submit">Iniciar sesión</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
  components: {

  },
  data(){
    return {
      email: '',
      password: '',
      valid: true,
      showpassword: false,
      emailRules:
            [
                email => !!email || "E-mail requerido",
                email => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email) || "E-mail inválido"
            ]
    }
  },
  methods: {
    login () {
      const path = 'http://127.0.0.1:8000/auth/'

      axios.post(path, {
         username: this.email,
         password: this.password,
      })
       .then((response) => {
         localStorage.setItem('user-token', response.data.token)

          swal(`¡Bienvenido ${this.email}!`, '', 'success')
          .then((response) =>{
            this.$router.push('/')
          })
       })
       .catch((response) => {
         localStorage.removeItem('user-token')
         swal("Error al iniciar sesión", '', 'error')
       })
    },

    validateForm () {
      this.$refs.form.validate()
    },
    submit () {
      this.validateForm()
      if(this.valid){
        this.login()
      }
    },
  }
}
</script>

<style scoped>



</style>
