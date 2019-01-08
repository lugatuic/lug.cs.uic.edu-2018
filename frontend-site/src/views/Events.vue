<template>
  <v-container grid-list-lg>
    <v-layout row>
      <v-flex>
        Search Card here
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex class="text-xs-center" v-if="events.length === 0">
        No events found.
      </v-flex>
      <template v-else>
        <v-flex
          v-for="(event, i) in viewableEvents"
          :key="i"
          xs12 md6>
          <event-card :event="event"/>
        </v-flex>
      </template>
    </v-layout>
    <v-layout row>
      <v-flex class="text-xs-center">
        <v-pagination v-model="currentPage" :length="numPages"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import EventCard from '@/components/Events/EventCard';

export default {
  components: {
    EventCard,
  },
  computed: {
    ...mapState(['useLightTheme']),
    ...mapState('events', {
      events: 'data',
    }),
    eventsPerPage: () => 15,
    numPages () {
      return Math.ceil(this.events.length / this.eventsPerPage);
    },
    viewableEvents () {
      const startIndex = (this.currentPage - 1) * this.eventsPerPage;
      const endIndex = startIndex + this.eventsPerPage;
      return this.events.filter((e, i) => i >= startIndex && i < endIndex);
    },
  },
  methods: {
    ...mapActions('events', ['updateData']),
  },
  data () {
    return {
      currentPage: 1,
    };
  },
  async mounted () {
    await this.updateData();
  },
};
</script>
