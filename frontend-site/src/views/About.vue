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
            <v-btn flat to="/office-policy">
              Office Policy
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
                    href="mailto:lug-uic-officers@googlegroups.com">
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
        <v-card>
          <v-card-title primary-title>
            <h1 class="title">Administration History</h1>
          </v-card-title>
          <v-divider/>
          <v-card-text v-if="isLoading" class="text-xs-center">
            <v-progress-circular indeterminate/>
            <h1 class="subheading">Loading Officer Data...</h1>
          </v-card-text>
          <v-expansion-panel v-else id="administration-history-list">
            <v-expansion-panel-content
              v-for="semester in semesters"
              :key="semester"
              lazy>
              <h1 class="title" slot="header" style="text-transform: capitalize;">{{ semester.replace(/_/g, ' ').toLowerCase() }}</h1>
              <v-card-text>
                <v-container fluid class="pa-0" grid-list-md>
                  <officer-listing :inputOfficers="officersBySemester[semester]"/>
                </v-container>
              </v-card-text>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';
import {
  positionOrder,
  convertSemesterToMonthStart,
  getNextSemester,
} from '@/modules/officers';
import OfficerListing from '@/components/Home/OfficerListing';

export default {
  components: {
    OfficerListing,
  },
  data () {
    return {
      officersBySemester: {},
      semesters: [],
      isLoading: true,
    };
  },
  methods: {
    ...mapActions('officers', ['updateData']),
    async initializeOfficerData () {
      const officers = await this.updateData();

      // sort by oldest to newest (by term_start)
      const sortedOfficers = officers.slice()
        .sort((a, b) => convertSemesterToMonthStart(a.term_start) - convertSemesterToMonthStart(b.term_start));

      const startSemester = sortedOfficers[0].term_start;
      const endSemester = getNextSemester(sortedOfficers[sortedOfficers.length - 1].term_start);

      // iteratively go through each semester and filter officers by semester
      for (let semester = startSemester; semester !== endSemester; semester = getNextSemester(semester)) {
        const currentSemesterDate = convertSemesterToMonthStart(semester);

        // get officers that serve by each term sorted by position
        this.officersBySemester[semester] = sortedOfficers.filter(officer => {
          const startTerm = convertSemesterToMonthStart(officer.term_start);
          const endTerm = convertSemesterToMonthStart(officer.term_end);
          return startTerm <= currentSemesterDate && endTerm >= currentSemesterDate;
        })
        .sort((a, b) => positionOrder.indexOf(a.position) - positionOrder.indexOf(b.position));
        this.semesters.push(semester);
      }

      this.semesters.reverse(); // show newest first
    },
  },
  async mounted () {
    try {
      await this.initializeOfficerData();
    } catch (err) {
      console.error(err);
    } finally {
      this.isLoading = false;
    }
  },
};
</script>

<style lang="scss">
#administration-history-list .officer-card {
  background-color: var(--card-default-background-color--darken-1)!important;
}
</style>
