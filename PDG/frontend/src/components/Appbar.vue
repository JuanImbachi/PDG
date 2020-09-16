<template>
  <div class="ownAppbar">
    <v-app-bar app dark>
        <v-app-bar-nav-icon style="font=white" @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>
          <router-link tag="span" to="/" style="cursor:pointer"> Dengue - Seguimiento de Casos </router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn class="mx-2" v-if="false"> <v-icon left>mdi-account-plus-outline</v-icon>New Register </v-btn>
        <v-btn class="pa-4" to="/login"  small outlined dark> Iniciar Sesión <v-icon right >mdi-account-lock</v-icon> </v-btn>
    </v-app-bar>

      <v-navigation-drawer app v-model="drawer" temporary dark>
        <v-list >
          <v-list-item :to="'/'">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
               <router-link tag="span" to="/" style="cursor:pointer">Inicio</router-link>
            </v-list-item-title>
          </v-list-item>
            <v-list-group
              v-for="item in items"
              :key="item.title"
              v-model="item.active"
              prepend-icon= "mdi-account-group"
              no-action
            >
              <template v-slot:activator >
                <v-list-item-content>
                  <v-list-item-title v-text="item.title"></v-list-item-title>
                </v-list-item-content>
              </template>

              <v-list-item
                v-for="subItem in item.cities"
                :key="subItem.title"
                :to="'/city/'+subItem.title"
              >
                <v-list-item-content>
                  <router-link v-bind:to="'/city/'+subItem.title" tag="span">{{subItem.title}}</router-link>
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
          </v-list>

          <v-list-item :to="'/test'">
            <v-list-item-icon>
              <v-icon>mdi-information-outline</v-icon>
            </v-list-item-icon>

            <v-list-item-title>
              Info
            </v-list-item-title>
          </v-list-item>
      </v-navigation-drawer>
  </div>
</template>


<script>
export default {
  name: "Toolbar",
  data() {
    return{
      drawer: false,
      items: [
          {
            title: 'Ciudades',
            cities: [
              { title: 'Buga'},
              { title: 'Cali'},
              { title: 'Girón'},
              { title: 'Palmira'},
              { title: 'Yopal'},
            ],
          },

      ]
    }
  },
  methods: {

  },
}
</script>

<style>
  .ownAppbar{
    margin-bottom: 7%;
  }
</style>
