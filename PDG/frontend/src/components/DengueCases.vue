<template>
  <v-container>
      <v-alert
        v-if=" newAppointmentStatus != null"
        :type="newAppointmentStatus.type"
        outlined
        text
        :icon="newAppointmentStatus.icon"
        transition="scale-transition"
      >
      {{newAppointmentStatus.message}}
      </v-alert>

      <v-toolbar dark>
        <v-toolbar-title>Casos Históricos de Dengue</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-dialog v-model="modal" :persistent="true">
          <NewDengueCaseForm  v-if="modal" @notifyNewAppointment="refresh" @notifyNewAppointmentStatus="showNewAppointmentStatus" @closeAppointmentForm="closeAppointmentForm"></NewDengueCaseForm>
        </v-dialog>
        <v-btn rounded @click="modal=!modal"><v-icon left>mdi-plus</v-icon>Agregar Caso</v-btn>
      </v-toolbar>
      <v-data-table
        :headers="headers"
        :items="dengueCases"
        item-key="id"
        class="elevation-1"
        :search="search"
        :custom-filter="filterText"
        calculate-widths:true
      >
      <template v-slot:top>
          <v-text-field v-model="search" label="Search" class="mx-4"></v-text-field>
      </template>
      </v-data-table>
    </v-container>
</template>

<script>
import NewDengueCaseForm from './NewDengueCaseForm'

export default {
  data() {
    return {
      cases: ['1'],
      search: '',
      modal: false
    }
  },
  components:
  {
    NewDengueCaseForm
  },
    computed: {
      headers () {
        return [
          {
          text: "Date",
          sortable: true,
          value: "date",
          align: "center"
          },
          {
            text: 'Assigned_to',
            sortable: true,
            value: 'assigned_to.fullname',
            align: 'center'
          },
          {
            text: 'Pet',
            sortable: true,
            value: 'pet.name',
            align: 'center'
          },
          {
            text: 'Services',
            sortable: true,
            value: 'service.name',
            align: 'center'
          },
          { text: "", value: "actions", sortable: false, align: "center" }
        ]
      },
    },

}
</script>

<style>
.v-toolbar__title {
  align-content: center;
  font-size: 180%;
  color: white;
}
.v-dialog_content {
    overflow-y:hidden;
}
.actionItems{
  float: left;
}
.itemAction{
  display: inline;
  margin-left: 20px;
}
.v-dialog {
    width: 50%;
}
</style>
