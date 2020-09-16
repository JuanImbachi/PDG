<template>
  <div>
    <h1>as</h1>
    <v-footer
      absolute
      class="font-weight-medium"
    >
      <v-col
        class="text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-col>
    </v-footer>
  </div>

</template>

<script>
export default {
  name: "Footer",
  data() {
    return {

    }
  },
}
</script>

<style>

</style>
