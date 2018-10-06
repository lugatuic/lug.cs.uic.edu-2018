<template>
  <v-toolbar
    app :clipped-left="false">
    <v-toolbar-side-icon @click="$emit('sidemenu-button-click')"/>
    <v-toolbar-title v-text="title"/>
    <v-spacer/>
    <v-btn flat outline>
      <v-icon>person_add</v-icon>
      <span>Sign Up</span>
    </v-btn>
    <v-btn icon>
      <v-icon>fab fa-slack</v-icon>
    </v-btn>
  </v-toolbar>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: '',
    },
  },
};
</script>

<style>

</style>
