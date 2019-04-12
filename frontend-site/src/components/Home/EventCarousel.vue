<template>
  <v-carousel
    class="event-carousel"
    v-model="activeEvent"
    hide-delimiters
    :interval="5000"
    :light="useLightTheme">
    <v-carousel-item v-for="(event, i) in events" :key="i">
      <event-card :event="event" :flat="true"/>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import EventCard from '@/components/Events/EventCard';
import debounce from 'lodash/debounce';
export default {
  components: {
    EventCard,
  },
  computed: {
    ...mapState(['useLightTheme']),
    ...mapState('events', {
      events: 'data',
    }),
    defaultCardHeight: () => 100,
  },
  data () {
    return {
      activeEvent: -1,
      height: 100,
      debouncedUpdateHeight: null,
      cardHeights: new Map(),
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

        // only set card height for valid events
        if (this.events[this.activeEvent]) {
          this.cardHeights.set(this.events[this.activeEvent], activeCard.offsetHeight);
        }
        const newHeight = Math.max(this.defaultCardHeight, ...Array.from(this.cardHeights.values()));
        if (newHeight !== this.height) {
          this.height = newHeight;
        }

        // update height of current card if its lesser than saved height
        if (activeCard.offsetHeight < this.height) {
          activeCard.style.height = `${this.height}px`;
        }
      }
    },
  },
  async mounted () {
    await this.updateData();
    this.activeEvent = 0;

    // debounced in case multiple EH fire simultaneously
    this.debouncedUpdateHeight = debounce(() => this.updateHeight(), 1000);
  },
  watch: {
    height (newValue) {
      console.warn(newValue);
      this.$el.style.height = `${newValue}px`;
    },
    activeEvent () {
      this.debouncedUpdateHeight();
    },
  },
};
</script>

<style lang="scss">
.event-carousel {
  background-color: var(--card-default-background-color);
  height: 150px; // default
  transition: height 0.5s;
}
</style>
