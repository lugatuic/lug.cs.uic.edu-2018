<template>
  <v-carousel class="event-carousel">
    <v-carousel-item v-for="(event, i) in events" :key="i">
      <v-card raised class="event-carousel-card">
        <v-card-title>
          {{ event.title }}
        </v-card-title>
        <v-card-text>
          {{ event }}
        </v-card-text>
      </v-card>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  computed: {
    events () {
      console.warn('using mock event data');
      // TODO: finalize format of events
      return [
        {
          title: 'event 1',
          description: 'this is a sample event',
          timing: 'Jan 01 1969 12 AM - 1 AM',
        },
        {
          title: 'event 2',
          description: 'this is a sample event',
          timing: 'Jan 01 1969 12 AM - 1 AM',
        },
        {
          title: 'event 3',
          description: 'this is a sample event',
          timing: 'Jan 01 1969 12 AM - 1 AM',
        },
      ];
    },
  },
};
</script>

<style lang="scss">
.event-carousel {
  // TODO: determine a good size, or do programmatically?
  height: 300px;
  .event-carousel-card {
    height: 100%;
  }
}
</style>
