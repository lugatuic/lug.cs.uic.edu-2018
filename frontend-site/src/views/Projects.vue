<template>
  <v-container grid-list-lg>
    <v-layout row>
      <v-flex>
        <search-card
          :allProjects="allProjects"
          v-model="projects"
        />
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex
        v-for="(project, i) in projects"
        :key="i"
        xs12 md6 lg3>
        <!-- TODO: refactor into separate component -->
        <v-card @click.native="activeProject = project" class="project-card">
          <!-- would put v-img or other image element here -->
          <v-container style="border: 1px solid white;">
            {{ project.smallImage }}
          </v-container>
          <v-card-title primary-title>
            <h1 class="headline">{{ project.name }}</h1>
          </v-card-title>
          <v-card-text class="text-xs-right pt-0">
            <h2 class="subheading">{{ project.status.toUpperCase() }}</h2>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="showModal">
      <v-card v-if="activeProject">
        <v-card-text>
          <v-container fluid>
            <v-layout row wrap>
              <v-flex xs12 md7>
                {{ activeProject.largeImage }}
              </v-flex>
              <v-flex xs12 md5>
                <h1 class="title">{{ activeProject.name }}</h1>
                <p>{{ activeProject.description }}</p>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn flat>GitHub</v-btn>
          <v-btn flat>Wiki</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mockProjects } from '@/modules/mockData';
import SearchCard from '@/components/Projects/SearchCard';

export default {
  components: {
    SearchCard,
  },
  computed: {
    // a master list of all projects
    allProjects: () => mockProjects,
  },
  data () {
    return {
      activeProject: null,
      showModal: false,
      projects: [],
    };
  },
  created () {
    this.projects = this.allProjects.slice();
  },
  mounted () {
    console.warn('using mock data for projects');
  },
  watch: {
    activeProject (newValue) {
      console.debug(newValue);
      if (newValue) {
        this.showModal = true;
      }
    },
    showModal (newValue) {
      if (!newValue) {
        this.activeProject = null;
      }
    },
    allProjects (newValue) {
      this.projects = newValue.slice();
    },
  },
};
</script>

<style lang="scss">
.project-card {
  cursor: pointer;
  & > * {
    pointer-events: none;
  }
}
</style>


