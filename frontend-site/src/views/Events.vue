<template>
  <h1>This is the events page. {{ events }}</h1>
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
  methods: {
    ...mapActions('events', ['updateData']),
  },
  async mounted () {
    await this.updateData();
  },
};
</script>
