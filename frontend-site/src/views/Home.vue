<template>
  <v-container grid-list-md>
    <v-layout justify-center>
      <lug-banner-svg class="full-logo mb-4"/>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12 sm6 md8 xl9>
        <h1 class="title">About</h1>
        <p>
          The LUG description goes here.
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Consectetur libero id faucibus nisl tincidunt eget nullam non. Velit aliquet sagittis id consectetur purus ut faucibus.
          Feugiat pretium nibh ipsum consequat nisl vel pretium.
          </p>
      </v-flex>
      <v-flex xs12 sm6 md4 xl3>
        <h1 class="title">Location</h1>
        <p>
          The LUG location goes here.
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </v-flex>
    </v-layout>
    <v-layout column align-center>
      <img src="@/assets/logo.png" alt="Vuetify.js" class="mb-5">
      Welcome to the home page.
      <!-- Suggestion: these view components should contain mostly other components; actual component implementations should be their own components -->
    </v-layout>
  </v-container>
</template>

<script>
import LugBannerSvg from '@/components/LugBannerSvg';

export default {
  components: {
    LugBannerSvg,
  },
};
</script>


<style lang="scss">
.full-logo {
  max-width: 100%;
}
</style>
