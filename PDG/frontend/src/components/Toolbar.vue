<template>
<div>
  <v-toolbar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>SGTCD - Palmira</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="mx-2"> Sign In </v-btn>
      <v-btn class="mx-2" color="primary"> Sign Up </v-btn>

    </v-toolbar>
    <v-navigation-drawer app v-model="drawer" temporary>
       <v-list>
         <v-list-item>
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>

          <v-list-item-title>Home</v-list-item-title>
        </v-list-item>
          <v-list-group
            v-for="item in items"
            :key="item.title"
            v-model="item.active"
            prepend-icon= "mdi-account-group"
            no-action
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item
              v-for="subItem in item.comunas"
              :key="subItem.title"
              @click=""
            >
              <v-list-item-content>
                <v-list-item-title v-text="subItem.title"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
        </v-list>

        <v-list-item>
          <v-list-item-icon>
            <v-icon>mdi-information-outline</v-icon>
          </v-list-item-icon>

          <v-list-item-title>More info</v-list-item-title>
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
            title: 'Comunas',
            comunas: [
              { title: 'Comuna 1' },
              { title: 'Comuna 2' },
              { title: 'Comuna 3' },
              { title: 'Comuna 4' },
              { title: 'Comuna 5' },
              { title: 'Comuna 6' },
              { title: 'Comuna 7' },
              { title: 'Comuna 8' },
            ],
          },

      ]
    }
  }
}
</script>

<style>

</style>
