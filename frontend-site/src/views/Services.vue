<template>
  <v-container grid-list-lg>
    <v-layout row wrap>
      <v-flex xs12 sm6 md4 v-for="(service, i) in services" :key="i">
        <!-- TODO: refactor separate component? -->
        <v-card class="ma-2">
          <v-container fluid class="pa-0">
            <v-layout row align-center>
              <v-flex xs5>
                <v-img :src="service.image"/>
              </v-flex>
              <v-flex xs5>
                <div style="border: 1px solid white; height: 100%;">
                <v-img :src="service.image"></v-img>
                </div>
              </v-flex>
              <v-flex xs7 class="pr-3">
                <h1 class="title">{{ service.name }}</h1>
                <p>{{ service.description || 'No description specified' }}</p>
                <v-card-actions v-if="service.url">
                  <v-spacer/>
                  <v-btn flat :href="service.url">More Info</v-btn>
                </v-card-actions>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { servicesOffered } from '@/modules/staticData';
export default {
  computed: {
    services: () => servicesOffered,
  },
};
</script>
