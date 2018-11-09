<template>
  <v-card class="project-search-card">
    <v-container fluid>
      <v-text-field
        v-model="filterOptions.textQuery"
        label="Name/Description Search"
        persistent-hint
        :hint="resultText"/>
    </v-container>
    <v-divider/>
    <v-expansion-panel>
      <v-expansion-panel-content>
        <div slot="header">Filter</div>
        <v-container fluid>
          <v-layout row wrap>
            <v-flex xs12>
              <h2 class="subheading">Status</h2>
            </v-flex>
            <v-flex v-for="(statusValue, i) in statusValues" :key="i">
              <v-checkbox v-model="filterOptions.status" :label="statusValue" :value="statusValue.toLowerCase()"/>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12>
              <h2 class="subheading">Wiki</h2>
            </v-flex>
            <v-flex v-for="(value, i) in wikiValues" :key="i">
              <v-checkbox v-model="filterOptions.wiki" :label="value" :value="value"/>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12>
              <h2 class="subheading">GitHub</h2>
            </v-flex>
            <v-flex v-for="(value, i) in githubValues" :key="i">
              <v-checkbox v-model="filterOptions.github" :label="value" :value="value"/>
            </v-flex>
          </v-layout>
        </v-container>
      </v-expansion-panel-content>
      <v-expansion-panel-content>
        <div slot="header">Sort</div>
        <v-container fluid>
          <v-layout row>
            <v-flex>
              <h2 class="subheading">Sort Type</h2>
              <v-radio-group
                v-model="sortOptions.type"
                :row="$vuetify.breakpoint.smAndUp">
                <v-radio
                  v-for="(type, i) in sortTypes"
                  :key="i"
                  :label="type"
                  :value="type"/>
              </v-radio-group>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex>
              <h2 class="subheading">Sort Order</h2>
              <v-radio-group
                v-model="sortOptions.isAscending"
                :row="$vuetify.breakpoint.smAndUp">
                <v-radio label="Ascending" :value="true"/>
                <v-radio label="Descending" :value="false"/>
              </v-radio-group>
            </v-flex>
          </v-layout>
        </v-container>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-card>
</template>

<script>
import * as projectValues from '@/modules/projectValues';
import { arraysAreEquivalent } from '@/modules/utils';
import debounce from 'lodash/debounce';

export default {
  props: {
    allProjects: {
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
    sortTypes: () => ['Name', 'Status', 'Date'],
    statusValues: () => projectValues.statusFilterValues,
    wikiValues: () => projectValues.wikiLinkFilterValues,
    githubValues: () => projectValues.gitHubLinkFilterValues,
    sorts: () => ({
      Name: (a, b, isAscending) => {
        const result = a.name < b.name ? -1 : 1;
        return isAscending ? result : -result;
      },
      // Status: (a, b, isAscending) => {
      //   const [indexA, indexB] = [this.statusFilterValues.m]
      // },
    }),
    // hasAnyFilters () {
    //   return [
    //     !!this.filterOptions.textQuery,
    //     this.filterOptions.status.length !== this.statusValues,
    //     this.filterOptions.wiki.length !== this.wikiValues,
    //     this.filterOptions.github.length !== this.githubValues,
    //   ].some(v => v);
    // },
  },
  data () {
    return {
      sortOptions: {
        type: 'Name',
        isAscending: true,
      },
      filterOptions: {
        textQuery: '',
        status: projectValues.statusFilterValues.map(v => v.toLowerCase()),
        wiki: projectValues.wikiLinkFilterValues.slice(),
        github: projectValues.gitHubLinkFilterValues.slice(),
      },
    };
  },
  methods: {
    sendNewProjectList (newList = []) {
      this.$emit('input', newList);
    },
    applyFilters (input = []) {
      return input.filter(project => {
        const fitsTextQuery = !this.filterOptions.textQuery ||
          (project.name && project.name.toLowerCase().includes(this.filterOptions.textQuery.toLowerCase())) ||
          (project.description && project.description.toLowerCase().includes(this.filterOptions.textQuery.toLowerCase()));

        const fitsStatus = this.filterOptions.status.includes(project.status.toLowerCase());

        const fitsWiki = this.filterOptions.wiki.length === this.wikiValues.length || // all values
          (this.filterOptions.wiki[0] === 'Has Wiki Link' && project.wikiLink) ||
          (this.filterOptions.wiki[0] === 'Does Not Have Wiki Link' && !project.wikiLink);

        const fitsGitHub = this.filterOptions.github.length === this.githubValues.length || // all values
          (this.filterOptions.github[0] === 'Has GitHub Link' && project.githubLink) ||
          (this.filterOptions.github[0] === 'Does Not Have GitHub Link' && !project.githubLink);

        return [fitsTextQuery, fitsStatus, fitsWiki, fitsGitHub].every(v => v); // return projects that fit every filter
      });
    },
    applySorts (input = []) {
      const sortFunction = this.sorts[this.sortOptions.type] || this.sorts.Name;
      return input.slice().sort((a, b) => sortFunction(a, b, this.sortOptions.isAscending));
    },
    applyOptionsAndUpdate: debounce(function () {
      this.sendNewProjectList(this.applySorts(this.applyFilters(this.allProjects)));
    }, 500),
  },
  watch: {
    filterOptions: {
      deep: true,
      handler () {
        this.applyOptionsAndUpdate();
      },
    },
    value (newValue, oldValue) {
      if (!arraysAreEquivalent(newValue, oldValue)) {
        this.applyOptionsAndUpdate();
      }
    },
  },
};
</script>

<style lang="scss">
.project-search-card {
  .v-radio {
    flex: 1 1 auto; // even distribution of radio buttons across entire width
  }

  .v-input--checkbox .v-label {
    text-transform: capitalize; // capitalize checkbox labels
  }
}
</style>
