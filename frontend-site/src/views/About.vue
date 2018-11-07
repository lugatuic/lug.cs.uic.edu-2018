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
            As an organization we provide support for students who are interested in learning about Linux and the open source community.
            Our goal is to spread open source technology and grow as programmers and individuals and eventually be able to contribute to the open source community.
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
            LUG shares an office with the UIC ACM in SELE 2264. Meetings are in SELE 2260 unless otherwise announced.
          </v-card-text>
          <v-card-actions>
            <v-container fluid class="pa-0">
              <v-layout row wrap>
                <v-flex>
                  <v-btn
                    flat block target="_blank" rel="noopener"
                    href="https://lugatuic.slack.com/messages">
                    <v-icon left>fab fa-slack</v-icon>
                    Slack
                  </v-btn>
                </v-flex>
                <v-flex>
                  <v-btn
                    flat block target="_blank" rel="noopener"
                    href="https://github.com/lugatuic">
                    <v-icon left>fab fa-github</v-icon>
                    Github
                  </v-btn>
                </v-flex>
                <v-flex>
                  <v-btn
                    flat block target="_blank" rel="noopener"
                    href="mailto:lug@uic.edu">
                    <v-icon left>email</v-icon>
                    Email
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-actions>
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
