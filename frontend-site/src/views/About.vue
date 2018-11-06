<template>
  <v-container grid-list-lg>
    <v-layout>
      <v-flex>
        <v-card>
          <v-card-title primary-title>
            <h1 class="title">Who We Are</h1>
          </v-card-title>
          <v-card-text>
            who we are goes here.
          </v-card-text>
          <v-card-actions>
            <v-btn flat>Constitution</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex>
        <v-card>
          <v-card-title primary-title>
            <h1 class="title">What We Do</h1>
          </v-card-title>
          <v-card-text>
            What We Do goes here.
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex>
        <v-card>
          <v-card-title primary-title>
            <h1 class="title">Where Are We</h1>
          </v-card-title>
          <v-card-text>
            info about office location, social links (slack, github, etc.) goes here.
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex>
        listing of previous officers by semester goes here; potentially reuse officer listing component
      </v-flex>
    </v-layout>
  </v-container>
</template>
