<template>
  <v-toolbar
    class="app-bar"
    dark app :clipped-left="false">
    <v-toolbar-side-icon v-if="$vuetify.breakpoint.mdAndDown" @click="$emit('sidemenu-button-click')"/>
    <v-toolbar-title v-text="title"/>
    <v-spacer/>
    <!-- <v-btn flat outline>
      <v-icon class="mr-1">person_add</v-icon>
      <span>Sign Up</span>
    </v-btn> -->
    <v-btn icon href="https://lugatuic.slack.com/messages" target="_blank" rel="noopener">
      <v-icon>fab fa-slack</v-icon>
    </v-btn>
    <v-btn icon @click="toggleLightTheme()">
      <v-icon>invert_colors</v-icon>
    </v-btn>
  </v-toolbar>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  props: {
    title: {
      type: String,
      default: '',
    },
  },
  methods: {
    ...mapMutations(['toggleLightTheme']),
  },
};
</script>

<style lang="scss">
.app-bar.v-toolbar {
  background-color: black;
}
</style>
