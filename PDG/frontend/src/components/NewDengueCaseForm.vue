<template>
  <v-container>
    <v-card>
      <v-card-title>
        Nuevo Caso de Dengue
      </v-card-title>
      <v-card-text>

    <v-form>
      <v-select
      v-model="selectMonth"
      :items="months"
      :rules="[v => !!v || 'Item is required']"
      label="Mes Ocurrencia"
      required
    ></v-select>

    <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          :return-value.sync="date"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-combobox
              v-model="date"
              label="Fecha de Notificación"
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
    </v-form>
          </v-card-text>

    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
      date: '',
    }
  },
}
</script>

<style>

</style>
