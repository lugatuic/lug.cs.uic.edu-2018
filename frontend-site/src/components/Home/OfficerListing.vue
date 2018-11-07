
<template>
  <v-layout row wrap class="officer-listing">
    <template v-if="!isLoading">
      <v-flex
        xs12 sm6 md4
        v-for="(officer, i) in officers"
        :key="i">
        <officer-card :officer="officer"/>
      </v-flex>
      <v-flex v-if="officers.length === 0">
        <v-card class="text-xs-center">
          <v-card-text>No officer data found.</v-card-text>
        </v-card>
      </v-flex>
    </template>
    <v-flex v-else>
      <v-card class="text-xs-center">
          <v-card-text>Loading officer data...</v-card-text>
        </v-card>
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
    isLoading: true,
  }),
  async mounted () {
    try {
      this.officers = await lugApi.getOfficers({
        semester: this.currentSemester,
      });
    } catch (err) {
      console.error(err);
    } finally {
      this.isLoading = false;
    }
  },
};
</script>

<style>
.officer-listing .officer-card {
  height: 100%;
}

.officer-listing {
  background-image: url();
}
</style>
