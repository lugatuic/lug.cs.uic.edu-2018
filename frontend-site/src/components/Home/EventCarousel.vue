<template>
  <v-carousel class="event-carousel" v-model="activeEvent" hide-delimiters :cycle="false">
    <v-carousel-item v-for="(event, i) in events" :key="i">
      <event-card :event="event" :flat="true"/>
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
      height: 50,
    };
  },
  methods: {
    ...mapActions('events', ['updateData']),
    getActiveCarouselElement () {
      // assumption: only one card is active at a time
      return Array.from(this.$el.querySelectorAll('.v-carousel__item'))
        .find(e => e.style.display !== 'none'); // get visible carousel item, if any
    },
    updateHeight () {
      const activeElement = this.getActiveCarouselElement();
      if (activeElement) {
        // compare active height to stored height and update accordingly
        const activeCard = activeElement.querySelector('.event-card');
        const newHeight = Math.max(this.height, activeCard.offsetHeight, activeCard.clientHeight);
        if (newHeight > this.height) {
          this.height = newHeight;
        }
      }
    },
  },
  async mounted () {
    await this.updateData();
    this.activeEvent = 0;
  },
  watch: {
    height (newValue) {
      console.debug('height changed to', newValue);
      this.$el.style.height = `${newValue}px`;
    },
    activeEvent () {
      // wait 1 tick for animation to finish
      this.$nextTick().then(() => this.updateHeight());
    },
  },
};
</script>

<style lang="scss">
.event-carousel {
  background-color: var(--card-default-background-color);
}
</style>
