<template>
  <v-card class="officer-card">
    <v-card-title>
      <h1 class="title">{{ officer.name }}</h1>
    </v-card-title>
    <v-container fluid>
      {{ officer }}
    </v-container>
  </v-card>
</template>

<script>
export default {
  props: {
    officer: {
      type: Object,
      required: true,
    },
  },
};
</script>

