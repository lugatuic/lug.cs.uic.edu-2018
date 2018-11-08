<template>
  <v-card>
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
          Filters content
        </v-container>
      </v-expansion-panel-content>
      <v-expansion-panel-content>
        <div slot="header">Sort</div>
        <v-container fluid>
          <v-layout row wrap>
            <v-flex xs12 sm6>
              <h2 class="subheading">Sort Type</h2>
            </v-flex>
            <V-flex xs12 sm6>
              <h2 class="subheading">Sort Order</h2>
            </V-flex>
          </v-layout>
        </v-container>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-card>
</template>

<script>
export default {

}
</script>
