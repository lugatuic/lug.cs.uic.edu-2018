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
import lugApi from '@/modules/LugApi';

export default {
  components: {
    OfficerCard,
  },
  computed: {
    // TODO: factor out if other things need this
    currentSemester () {
      const currentDate = new Date();
      const currentMonth = currentDate.getMonth() + 1; // getMonth is 0 indexed, so add 1
      const currentYear = currentDate.getUTCFullYear();
      let currentSemester = '';
      if (currentMonth <= 5) { // up to May
        currentSemester = 'SPRING';
      } else if (currentMonth <= 8) { // up to August
        currentSemester = 'SUMMER';
      } else {
        currentSemester = 'FALL';
      }
      return `${currentSemester}_${currentYear}`;
    },
  },
  data: () => ({
    officers: [],
  }),
  async mounted () {
    this.officers = await lugApi.getOfficers({
      semester: this.currentSemester,
    });
  },
};
</script>

<style>
.officer-listing .officer-card {
  height: 100%;
}
</style>
