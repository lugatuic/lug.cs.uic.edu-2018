
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
  props: {
    // specify a semester to initiate a remote query on component mount
    semester: {
      type: String,
      default: '',
    },
    inputOfficers: {
      type: Array,
      default: () => [],
    },
  },
  components: {
    OfficerCard,
  },
  data: () => ({
    officers: [],
    isLoading: true,
  }),
  async mounted () {
    try {
      if (this.semester) {
        this.officers = await lugApi.getOfficers({
          semester: this.semester,
        });
      } else {
        this.officers = this.inputOfficers.slice();
      }
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
