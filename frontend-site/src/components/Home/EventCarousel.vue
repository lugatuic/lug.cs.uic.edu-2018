<template>
  <v-carousel class="event-carousel" v-model="activeEvent" hide-delimiters>
    <v-carousel-item v-for="(event, i) in events" :key="i">
      <event-card :event="event"/>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import EventCard from '@/components/Home/EventCard';
export default {
  components: {
    EventCard,
  },
  computed: {
    ...mapState(['useLightTheme']),
    ...mapState('events', {
      events: 'data',
    }),
  },
  data () {
    return {
      activeEvent: -1,
    };
  },
  methods: {
    ...mapActions('events', ['updateData']),
  },
  async mounted () {
    await this.updateData();
    this.activeEvent = 0;
  },
};
</script>

<style lang="scss">
.event-carousel {
  // TODO: determine a good size, or do programmatically?
  height: 300px;
}
</style>
