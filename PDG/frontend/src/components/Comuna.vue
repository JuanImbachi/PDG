<template>
  <v-container>
    <div class="comunaContainer">
      <h1>This is the comuna {{id}}</h1>

    </div>
  </v-container>
</template>

<script>
export default {
   data() {
     return {
       id: ""
     }
   },
   methods: {
     getComunaId(){
       this.id = this.$route.params.id;

     }
   },
   created() {
     this.getComunaId();
   },
}
</script>

<style scope>

  .comunaContainer{
    background-color: rgba(128, 128, 128, 0.319);
  }
</style>
