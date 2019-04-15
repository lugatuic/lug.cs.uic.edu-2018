<template>
  <v-container grid-list-md class="home-page">
    <v-layout justify-center>
      <lug-banner-svg class="full-logo mb-4"/>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12 sm6 md8 xl9>
        <h1 class="title">About</h1>
        <span>
          LUG at UIC is a student organization whose purpose is to provide a community for students that are interested in all things related to Linux and open source.
          As a community we strive to provide the support and education that students seek.
          Through various events and activities we work towards building a bigger community and spreading the use of Linux and open source software.
        </span>
      </v-flex>
      <v-flex xs12 sm6 md4 xl3>
        <h1 class="title">Location</h1>
        <span>
          Office is located in SELE 2264.
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
        <officer-listing :semester="currentSemester"/>
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
import { getCurrentSemester } from '@/modules/officers';
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
  computed: {
    currentSemester: () => getCurrentSemester(),
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
