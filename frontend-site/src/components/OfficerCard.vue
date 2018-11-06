<template>
  <v-card :raised="!useLightTheme" class="officer-card">
    <v-img
      contain
      :alt="avatarAlt"
      :src="avatarUrl"
      aspect-ratio="2.75"/>
    <v-card-title>
      <div>
        <h1 class="title">{{ officerName }}</h1>
        <h2 class="subheading" style="text-transform: capitalize;">{{ officer.position.replace(/_/g, ' ').toLowerCase() }}</h2>
        <h3 class="subheading" style="text-transform: capitalize;">Term: {{ termsServingMessage }}</h3>
      </div>
    </v-card-title>
    <v-card-text>
      {{ officer.description }}
    </v-card-text>
    <v-card-actions v-if="hasSocialLinks">
      <v-spacer/>
      <v-btn
        v-if="officer.github"
        :href="officer.github"
        rel="noopener"
        target="_blank"
        icon>
        <v-icon>fab fa-github</v-icon>
      </v-btn>
      <v-btn
        v-if="officer.personal_site"
        :href="officer.personal_site"
        rel="noopener"
        target="_blank"
        icon>
        <v-icon>fa fa-link</v-icon>
      </v-btn>
      <v-spacer/>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapState } from 'vuex';

export default {
  props: {
    officer: {
      type: Object,
      required: true,
    },
  },
  computed: {
    ...mapState(['useLightTheme']),
    defaultAvatarUrl () {
      return this.useLightTheme ? require('@/assets/blackTux.png') : require('@/assets/whiteTux.png');
    },  
    avatarUrl () {
      return this.officer.image || this.defaultAvatarUrl;
    },
    avatarAlt () {
      return `${this.officer.name}'s image`;
    },
    officerName () {
      return [
        this.officer.name,
        this.officer.slack ? `(@${this.officer.slack})` : undefined,
      ].filter(v => v) // remove empty values
      .join(' ');
    },
    hasSocialLinks () {
      return [
        this.officer.github,
        this.officer.personal_site,
      ].some(v => v); // look for any truthy values
    },
    termsServingMessage () {
      return [
        this.officer.term_start.replace(/_/g, ' '),
        this.officer.term_end.replace(/_/g, ' '),
      ].join('-');
    },
  },
};
</script>
