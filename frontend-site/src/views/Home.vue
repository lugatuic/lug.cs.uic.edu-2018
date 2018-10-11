<template>
  <v-container fluid>
    <v-layout justify-center>
      <object type="image/svg+xml" :data="require('@/assets/LUG_logo_Non-UIC.svg')" class="full-logo">
        LUG Logo
      </object>
    </v-layout>
    <v-layout column align-center>
      <img src="@/assets/logo.png" alt="Vuetify.js" class="mb-5">
      Welcome to the home page.
      <!-- Suggestion: these view components should contain mostly other components; actual component implementations should be their own components -->
    </v-layout>
  </v-container>
</template>

<style lang="scss">
.full-logo {
  path {
    fill: green!important;
  }
}
</style>
