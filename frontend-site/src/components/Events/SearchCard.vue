<template>
  <v-card>
    <v-container fluid>
      <v-layout row wrap align-center>
        <v-flex>
          <v-text-field
            v-model="filterOptions.textQuery"
            label="Name/Description Search"
            persistent-hint
            :hint="resultText"/>
        </v-flex>
        <v-flex style="flex: 0 1 auto;">
          <v-layout row align-center>
            <v-flex>
              <v-select
                :items="sortTypes"
                label="Sort By"
                persistent-hint
                :hint="sortText"
                v-model="sortOptions.type"/>
            </v-flex>
            <v-flex>
              <v-btn flat icon @click="sortOptions.isAscending = !sortOptions.isAscending">
                <v-icon :style="`transform: scaleY(${sortOptions.isAscending ? -1 : 1})`">sort</v-icon>
              </v-btn>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>
import { arraysAreEquivalent } from '@/modules/utils';
import debounce from 'lodash/debounce';

export default {
  props: {
    allEvents: {
      type: Array,
      required: true,
    },
    value: {
      type: Array,
      required: true,
    },
  },
  computed: {
    resultText () {
      return `${this.value.length} ${this.value.length === 1 ? 'result' : 'results'}`;
    },
    sortText () {
      return this.sortOptions.isAscending ? 'Ascending' : 'Descending';
    },
    sortTypes: () => ['Name', 'Start Time', 'End Time'],
    sorts: () => ({
      Name: (a, b, isAscending) => {
        const result = a.summary < b.summary ? -1 : 1;
        return isAscending ? result : -result;
      },
      'Start Time': (a, b, isAscending) => {
        const diff = new Date(a.timeStart) - new Date(b.timeStart);
        return isAscending ? diff : -diff;
      },
      'End Time': (a, b, isAscending) => {
        const diff = new Date(a.timeEnd) - new Date(b.timeEnd);
        return isAscending ? diff : -diff;
      },
    }),
  },
  data () {
    return {
      sortOptions: {
        type: 'Start Time',
        isAscending: true,
      },
      filterOptions: {
        textQuery: '',
      },
    };
  },
  methods: {
    sendFilteredList (newList = []) {
      this.$emit('input', newList);
    },
    applySorts (input = []) {
      const sortFunction = this.sorts[this.sortOptions.type] || this.sorts.Name;
      return input.slice().sort((a, b) => sortFunction(a, b, this.sortOptions.isAscending));
    },
    applyChangesAndUpdate: debounce(function () {
      this.sendFilteredList(this.applySorts(this.allEvents));
    }, 500),
  },
  watch: {
    sortOptions: {
      deep: true,
      handler () {
        this.applyChangesAndUpdate();
      },
    },
    value (newValue, oldValue) {
      // apply current filters/sorts on new data input
      if (!arraysAreEquivalent(newValue, oldValue)) {
        this.applyChangesAndUpdate();
      }
    },
  },
};
</script>

<style>

</style>
