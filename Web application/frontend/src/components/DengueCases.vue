<template>
  <v-container mt-8>
      <v-toolbar class="blue-grey darken-1">
        <v-toolbar-title><b>Registros Históricos</b></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-dialog v-model="modal" :persistent="true">
          <NewDengueCaseForm  v-if="modal" @notifyNewCase="refresh" @closeDengueCaseForm="modal=!modal"></NewDengueCaseForm>
        </v-dialog>
        <v-btn rounded @click="modal=!modal" class="white black--text"><v-icon left>mdi-plus</v-icon>Agregar Caso</v-btn>
      </v-toolbar>
      <v-data-table
        :headers="headers"
        :items="cases"
        item-key="id"
        class="elevation-1"
        :search="search"
        calculate-widths:true
        no-data-text="Cargando..."
        no-results-text="No se encontraron registros"
      >

      <template v-slot:top>
          <v-text-field v-model="search" label="Search" class="mx-4"></v-text-field>
      </template>
      <template  v-slot:item.actions="{ item }">
        <v-icon
          small
          color="error"
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      </v-data-table>

    </v-container>
</template>

<script>
import NewDengueCaseForm from './NewDengueCaseForm'
import swal from 'sweetalert'
import apiDengue from "@/apiDengue";

export default {
  data() {
    return {
      headers: [
        {
          text: 'Ciudad',
          align: 'center',
          sortable: true,
          value: 'City',
        },
        {
          text: 'Fecha Notificación',
          sortable: true,
          value: 'NotificationDate',
          align: 'center'
        },
        {
          text: 'Edad',
          sortable: false,
          value: 'Age',
          align: 'center'
        },
        {
          text: 'Género',
          sortable: false,
          value: 'Gender',
          align: 'center'
        },
        {
          text: 'Barrio',
          sortable: true,
          value: 'Neighborhood',
          align: 'center'
        },
        {
          text: 'Comuna',
          sortable: false,
          value: 'Commune',
          align: 'center'
        },
        {
          sortable: false,
          value: 'actions',
        },
      ],
      cases: [],
      search: '',
      modal: false,
      editedIndex: -1,
      editedItem : {}
    }
  },
  methods: {
    getCases () {
      apiDengue.getCases().then((response) => {
        this.cases = response.data
      })
      .catch((error=>{
        console.log(error)
      }))
    },

    deleteItem (item) {
      this.editedIndex = this.cases.indexOf(item)
      this.editedItem = Object.assign({}, item)

      swal({
        title: "¿Está Seguro?",
        text: "¿Una vez eliminado este registro no se podrá recuperar!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          this.deleteItemConfirm()
        } else {
          swal({title: "Cambios no guardados", icon: "warning",});
        }
      })

    },

    deleteItemConfirm () {
      apiDengue.deleteCase(this.editedItem.id).then((response) => {
        this.cases.splice(this.editedIndex, 1)
        this.$nextTick(() => {
          this.editedIndex = -1
        })
        swal("¡Registrado eliminado exitosamente!", '', 'success')
      })
      .catch((error) =>{
        console.log(error)
        swal({title: "No fue posible eliminar el registro", icon: "error",});
      })
    },

    async refresh() {
      this.cases = []
      this.getCases()
      this.modal = !this.modal
    }
  },
  created() {
    this.getCases()
  },
  watch: {
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },
  components:
  {
    NewDengueCaseForm
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
