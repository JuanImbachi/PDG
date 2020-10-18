<template>
  <v-container>
    <v-card>
      <v-card-title class="grey darken-4 white--text">
        Registrar Nuevo Caso
      </v-card-title>
      <v-card-text>

    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
      >
      <v-select
      v-model="city"
      :items="cities"
      :rules="[v => !!v || 'Item is required']"
      label="Ciudad"
      required
      ></v-select>
      <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-combobox
              v-model="date"
              label="Fecha de Notificación"
              :rules="[v => !!v || 'Item is required']"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-combobox>
          </template>
          <v-date-picker
            v-model="date"
            no-title
            scrollable
            >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="menu = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.menu.save(date)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
        <v-text-field
          v-model="age"
          :rules="[v => !!v || 'Age is required']"
          label="Edad"
          required
          type="number"
          min=0
        ></v-text-field>
        <v-select
          v-model="neighborhood"
          :items="neighborhoods"
          :rules="[v => !!v || 'Item is required']"
          label="Barrio"
          required
        ></v-select>
        <v-select
          v-model="gender"
          :items="genders"
          :rules="[v => !!v || 'Item is required']"
          label="Género"
          required
        ></v-select>
      </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          @click="validate"
        >
          Guardar
        </v-btn>

        <v-btn
          color="error"
          class="mr-4"
          @click="cancel"
        >
          Cancelar
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      menu: false,
      valid: true,
      months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
      cities: ['Buga', 'Yopal', 'Girón'],
      genders: ['Femenino', 'Masculino'],
      neighborhoods: ['Mercedes'],
      city: '',
      date: '',
      age: '',
      neighborhood: '',
      gender: '',
    }
  },
  methods: {
    validate () {
        if(this.$refs.form.validate()){
          alert("valid")
        }
      },
      reset () {
        this.$refs.form.reset()
      },

      cancel () {
        this.reset()
        this.$emit("closeAppointmentForm")
      }
  },

}
</script>

<style>

</style>
