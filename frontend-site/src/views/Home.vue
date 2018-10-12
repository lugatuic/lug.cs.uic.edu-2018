<template>
  <v-container grid-list-md class="home-page">
    <v-layout justify-center>
      <lug-banner-svg class="full-logo mb-4"/>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12 sm6 md8 xl9>
        <h1 class="title">About</h1>
        <span>
          The LUG description goes here.
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Consectetur libero id faucibus nisl tincidunt eget nullam non. Velit aliquet sagittis id consectetur purus ut faucibus.
          Feugiat pretium nibh ipsum consequat nisl vel pretium.
        </span>
      </v-flex>
      <v-flex xs12 sm6 md4 xl3>
        <h1 class="title">Location</h1>
        <span>
          The LUG location goes here.
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </span>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12>
        <h1 class="title">Events</h1>
      </v-flex>
      <v-flex xs12>
        <event-carousel/>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12>
        <h1 class="title">Main Officers</h1>
      </v-flex>
      <v-flex xs12>
        <officer-listing/>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12>
        <h1 class="title">Utilities</h1>
      </v-flex>
      <v-flex xs12>
        <utilities-listing/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import LugBannerSvg from '@/components/LugBannerSvg';
import EventCarousel from '@/components/Home/EventCarousel';
import OfficerListing from '@/components/Home/OfficerListing';
import UtilitiesListing from '@/components/Home/UtilitiesListing';

export default {
  components: {
    LugBannerSvg,
    EventCarousel,
    OfficerListing,
    UtilitiesListing,
  },
};
</script>


<style lang="scss">
.home-page {
  .full-logo {
    max-width: 100%;
  }

  .flex > h1.title {
    margin-top: 1rem;
  }

}
</style>
