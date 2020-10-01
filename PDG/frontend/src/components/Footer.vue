<template>
   <v-footer
        absolute
        padless
        dark
        class="mt-2"
      >
      <v-card
          class="flex"
          flat
          tile
        >
        <v-card-text class="py-2 white--text text-center">
            {{ new Date().getFullYear() }} — <strong>Universidad Icesi</strong>
          </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
export default {
  name: "Footer",
    data() {
      return{
      }
    }
}
</script>

<style>

</style>
