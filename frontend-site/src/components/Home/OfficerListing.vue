<template>
  <v-layout row wrap class="officer-listing">
    <v-flex
      xs12 sm6 md4
      v-for="(officer, i) in officers"
      :key="i">
      <officer-card :officer="officer"/>
    </v-flex>
  </v-layout>
</template>

<script>
import OfficerCard from '@/components/OfficerCard';
import { mapState, mapActions } from 'vuex';

export default {
  components: {
    OfficerCard,
  },
  computed: {
    ...mapState('officers', {
      officers: 'data',
    }),
  },
  methods: {
    ...mapActions('officers', ['updateData']),
  },
  async mounted () {
    await this.updateData();
  },
};
</script>

<style>
.officer-listing .officer-card {
  height: 100%;
}
</style>
