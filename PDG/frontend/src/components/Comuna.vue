<template>
  <v-container>
    <div class="comunaContainer">
      <h1>This is the comuna {{ getComunaId() }}</h1>
      <v-row>
        <v-col
          cols="12"
          md="8"
        >
          <v-card
            class="pa-2"
            outlined
            tile
          >
            .col-12 .col-md-8
          </v-card>
        </v-col>
        <v-col
          cols="6"
          md="4"
        >
          <v-card
            class="pa-2"
            outlined
            tile
          >
          <v-img :src="src" aspect-ratio="1.2" ></v-img>
          </v-card>
       </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
export default {
   data() {
     return {
       id: "",
       src: require('../assets/Palmira.png'),
     }
   },
   methods: {
     getComunaId(){
       this.id = this.$route.params.id
       return this.id;
     }
   },

}
</script>

<style scope>

  .comunaContainer{
    background-color: rgba(128, 128, 128, 0.319);
  }
</style>
