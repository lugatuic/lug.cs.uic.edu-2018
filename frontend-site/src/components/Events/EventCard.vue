<template>
  <v-card
    :dark="!useLightTheme"
    :light="useLightTheme"
    raised
    :flat="flat"
    class="event-card">
    <v-container fluid class="pl-5 pr-5">
      <v-layout row wrap>
        <v-flex xs12 sm6>
          <h1 class="headline">{{ event.summary }}</h1>
        </v-flex>
        <v-flex xs12 sm6>
          <h2 class="subheading">{{ dateHeading }}</h2>
          <h2 class="subheading">{{ locationDescription }}</h2>
        </v-flex>
      </v-layout>
      <v-layout>
        <v-flex>
          {{ eventDescription }}
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>
import { mapState } from 'vuex';

export default {
  props: {
    event: {
      type: Object,
      required: true,
    },
    flat: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    ...mapState(['useLightTheme']),
    isSameDate () {
      const startDate = new Date(this.event.timeStart);
      const endDate = new Date(this.event.timeEnd);
      return [
        startDate.getYear() === endDate.getYear(),
        startDate.getMonth() === endDate.getMonth(),
        startDate.getDate() === endDate.getDate(),
      ].every(isTrue => isTrue);
    },
    dateHeading () {
      if (this.isSameDate) {
        const startDate = new Date(this.event.timeStart);
        const endDate = new Date(this.event.timeEnd);
        return `${startDate.toLocaleDateString()}: ${startDate.toLocaleTimeString()} to ${endDate.toLocaleTimeString()}`;
      } else {
        return [
          new Date(this.event.timeStart).toLocaleString(),
          new Date(this.event.timeEnd).toLocaleString(),
        ].join(' to ');
      }
    },
    locationDescription () {
      return `Location: ${this.event.location || 'None Specified'}`;
    },
    eventDescription () {
      return this.event.description || 'No description specified';
    },
  },
};
</script>
