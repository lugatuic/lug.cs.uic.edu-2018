<template>
  <v-carousel
    class="event-carousel"
    v-model="activeEvent"
    hide-delimiters
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
  },
  data () {
    return {
      activeEvent: -1,
      height: 50,
      onAnimationEndHandler: null,
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
        const newHeight = Math.max(this.height, activeCard.offsetHeight);
        if (newHeight > this.height) {
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

    // shared instance for EH removal in beforeDestroy
    // debounced in case multiple EH fire simultaneously
    this.onAnimationEndHandler = debounce(() => this.updateHeight(), 50);

    // add event handler for after transitions finish to ensure only one card is visible when updating height
    Array.from(this.$el.querySelectorAll('.v-carousel__item')).forEach(item => {
      item.addEventListener('transitionend', this.onAnimationEndHandler);
      item.addEventListener('webkitTransitionEnd', this.onAnimationEndHandler);
    });
  },
  beforeDestroy () {
    Array.from(this.$el.querySelectorAll('.v-carousel__item')).forEach(item => {
      item.removeEventListener('transitionend', this.onAnimationEndHandler);
      item.removeEventListener('webkitTransitionEnd', this.onAnimationEndHandler);
    });
  },
  watch: {
    height (newValue) {
      this.$el.style.height = `${newValue}px`;
    },
  },
};
</script>

<style lang="scss">
.event-carousel {
  background-color: var(--card-default-background-color);
  height: 150px; // default
}
</style>
