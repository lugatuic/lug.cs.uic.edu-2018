<template>
  <v-container grid-list-lg>
    <v-layout row wrap>
      <v-flex xs12 v-for="(service, i) in services" :key="i">
        <!-- TODO: refactor into exparate component -->
        <v-card class="ma-2">
          <v-container fluid class="pa-0">
            <v-layout row>
              <v-flex xs6>
                <template v-if="i % 2 === 0">
                  <div style="border: 1px solid white; height: 100%;">
                    {{ service.image }}
                  </div>
                </template>
                <template v-else>
                  <h1 class="title">{{ service.name }}</h1>
                  <p>{{ service.description }}</p>
                </template>
              </v-flex>
              <v-flex xs6>
                <template v-if="i % 2 === 1">
                  <div style="border: 1px solid white; height: 100%;">
                    {{ service.image }}
                  </div>
                </template>
                <template v-else>
                  <h1 class="title">{{ service.name }}</h1>
                  <p>{{ service.description }}</p>
                </template>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mockServices } from '@/modules/mockData';
export default {
  computed: {
    services: () => new Array(12).fill(mockServices[0]),
  },
  mounted () {
    console.warn('using mock data for services');
  },
};
</script>
