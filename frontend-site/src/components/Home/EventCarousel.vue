<template>
  <v-carousel class="event-carousel" v-model="activeEvent" hide-delimiters>
    <v-carousel-item v-for="(event, i) in events" :key="i">
      <!-- TODO: move to separate component? -->
      <v-card
        :dark="!useLightTheme"
        :light="useLightTheme"
        raised
        class="event-carousel-card">
        <v-card-title>
          {{ event.summary }}<br>
          {{ new Date(event.timeStart).toLocaleString() }} to {{ new Date(event.timeEnd).toLocaleString() }}
        </v-card-title>
        <v-card-text>
          {{ event }}
        </v-card-text>
      </v-card>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  computed: {
    ...mapState(['useLightTheme']),
    ...mapState('events', {
      events: 'eventData',
    }),
  },
  data () {
    return {
      activeEvent: -1,
    };
  },
  methods: {
    ...mapActions('events', ['updateEventData']),
  },
  async mounted () {
    await this.updateEventData();
    this.activeEvent = 0;
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
