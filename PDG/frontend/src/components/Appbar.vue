<template>
  <div class="ownAppbar">
    <v-app-bar app >
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>
          <router-link tag="span" to="/" style="cursor:pointer"> SGTCD - Palmira </router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn class="mx-2"> <v-icon left>mdi-account-plus-outline</v-icon>New Register </v-btn>
        <v-btn class="mx-2" to="/login" color="primary" > <v-icon left>mdi-login</v-icon> Log In </v-btn>
    </v-app-bar>

      <v-navigation-drawer app v-model="drawer" temporary>
        <v-list>
          <v-list-item @click="clickListItem('')">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link tag="span" to="/">Home</router-link>
            </v-list-item-title>
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
                @click="clickListItem('comuna/' + subItem.id)"
              >
                <v-list-item-content>
                  <v-list-item-title v-text="subItem.title"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
          </v-list>

          <v-list-item  @click="clickListItem('Test')">
            <v-list-item-icon>
              <v-icon>mdi-information-outline</v-icon>
            </v-list-item-icon>

            <v-list-item-title>
              More Info
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
            title: 'Comunas',
            comunas: [
              { title: 'Comuna 1', id: 1 },
              { title: 'Comuna 2', id: 2 },
              { title: 'Comuna 3', id: 3 },
              { title: 'Comuna 4', id: 4 },
              { title: 'Comuna 5', id: 5 },
              { title: 'Comuna 6', id: 6 },
              { title: 'Comuna 7', id: 7 },
            ],
          },

      ]
    }
  },
  methods: {
    clickListItem(path){
      this.$router.push({path: '/'+path});
    }
  },
}
</script>

<style>
  .ownAppbar{
    margin-bottom: 7%;
  }
</style>
