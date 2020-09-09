<template>
      <v-container >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>Login</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    v-model="email"
                    label="Correo electrónico"
                    name="email"
                    prepend-icon="mdi-email"
                    type="email"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="password"
                    id="password"
                    label="Contraseña"
                    name="password"
                    prepend-icon="mdi-lock"
                    type="password"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="login">Iniciar sesión</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
</template>

<script>
import axios from 'axios'
export default {
  components: {

  },
  data(){
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:8000/auth/', {
        email: this.email,
        password: this.password,
      })
      .then(resp => console.log('it works!'))
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

.container {
    background-color: white;
}

</style>
