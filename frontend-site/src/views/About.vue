<template>
  <v-container grid-list-lg>
    <v-layout>
      <v-flex>
        <v-card>
          <v-card-title primary-title>
            <h1 class="title">Who We Are</h1>
          </v-card-title>
          <v-card-text>
            The Linux Users Group at University of Illinois at Chicago (LUG@UIC) is a student organization whose purpose is to provide a community for students that are interested in all things related to Linux and Open Source Technology.
            As a community we strive to provide the support and education that students seek.
            Through various events and activities we work towards building a bigger community and spreading the use of Linux and open source software.
          </v-card-text>
          <v-card-actions>
            <v-btn
            href="https://github.com/lugatuic/lug-docs/blob/master/rfc0000-lug-constitution.md"
            flat target="_blank"
            rel="noopener">
              Constitution
            </v-btn>
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
