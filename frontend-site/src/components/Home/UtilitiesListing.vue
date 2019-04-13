<template>
  <v-layout row wrap class="utility-listing">
    <v-flex
      xs6 sm4 md3
      v-for="(utility, i) in utilities"
      :key="i">
      <!-- TODO: move into another separate component or keep inline here? -->
      <v-card class="utility-card">
        <v-container fluid>
          <v-layout align-center align-content-center>
            <v-flex class="text-xs-center">
              <h1 class="title">{{ utility }}</h1>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { utilitiesOffered } from '@/modules/staticData';
export default {
  computed: {
    utilities: () => utilitiesOffered,
  },
};
</script>

<style lang="scss">
.utility-listing {
  justify-content: center;

  .utility-card {
    min-height: 100px;
  }
}
</style>
