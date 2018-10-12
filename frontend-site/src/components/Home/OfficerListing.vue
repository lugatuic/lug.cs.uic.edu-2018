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

export default {
  computed: {
    officers () {
      console.warn('using mock officer data');
      return [
        {
          name: 'Jane Doe',
          // picture: 'url goes here',
          bio: 'A bio would go nicely here. Should we allow HTML here or just plaintext?',
          position: 'President',
          special: 'Leads projects in directions',
        },
        {
          name: 'John Smith',
          // picture: 'url goes here',
          bio: 'A bio would go nicely here. Should we allow HTML here or just plaintext?',
          position: 'Vice President',
          special: 'Leads projects in other directions',
        },
        {
          name: 'Bob',
          // picture: 'url goes here',
          bio: 'A bio would go nicely here. Should we allow HTML here or just plaintext?',
          position: 'Treasurer',
          special: 'Gives money to people for useful things',
        },
      ];
    },
  },
  components: {
    OfficerCard,
  },
};
</script>

<style>
.officer-listing .officer-card {
  height: 100%;
}
</style>
