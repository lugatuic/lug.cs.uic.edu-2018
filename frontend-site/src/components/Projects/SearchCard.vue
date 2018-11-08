<template>
  <v-card class="project-search-card">
    <v-container fluid>
      <v-text-field
        label="Name/Description Search"
        persistent-hint
        hint="## results"/>
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

export default {
  computed: {
    sortTypes: () => ['Name', 'Status', 'Date'],
    statusValues: () => projectValues.statusFilterValues,
    wikiValues: () => projectValues.wikiLinkFilterValues,
    githubValues: () => projectValues.gitHubLinkFilterValues,
  },
  data () {
    return {
      textQuery: '',
      sortOptions: {
        type: 'Name',
        isAscending: true,
      },
      filterOptions: {
        status: projectValues.statusFilterValues.map(v => v.toLowerCase()),
        wiki: projectValues.wikiLinkFilterValues.slice(),
        github: projectValues.gitHubLinkFilterValues.slice(),
      },
    };
  },
  mounted () {
    console.debug(this.filterOptions);
  },
  watch: {
    filterOptions: {
      deep: true,
      handler (newValue) {
        console.debug(newValue);
      },
    },
  },
};
</script>

<style lang="scss">
.project-search-card {
  .v-radio {
    flex: 1 1 auto; // even distribution of radio buttons across entire width
  }
}
</style>
