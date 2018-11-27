<template>
  <v-container grid-list-lg>
    <v-layout row v-for="(policy, i) in policies" :key="i">
      <v-flex>
        <v-card>
          <v-card-title primary-title>
            <h1 class="title">{{ policy.name }}</h1>
          </v-card-title>
          <v-card-text>
            <span
              v-for="(entry, j) in policy.rules"
              :key="j"
              class="d-block"
              v-text="entry"/>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex>
        <v-card>
          <v-card-title primary-title>
            <h1 class="title">Space Policy</h1>
          </v-card-title>
          <v-card-text>
            <span class="d-block">
              The LUG office is a shared resource and thus, we have many people coming in any time during the day. While you are free to use the desks and chairs of the LUG office, you may not 'hog' a seat. You must give up your seat to another person that wants to do any of the following:
            </span>
            <ul>
              <li>Study</li>
              <li>Work</li>
              <li>SIG related educational activities</li>
              <li>Educating oneself (reading articles, newspapers, etc) NOT comics, reddit, digg, etc</li>
              <li>Developing</li>
            </ul>
            <span class="d-block">The LUG office has no assigned seats and therefore, you must pick up after yourself when you leave. If you are to leave momentarily, please leave a note so nobody takes your seat.</span>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex>
        <v-card>
          <v-card-title primary-title>
            <h1 class="title">Violations to the Policy</h1>
          </v-card-title>
          <v-card-text>
            <span class="d-block"><b>First time offenders:</b> You will not be allowed to use the office or the office resources for a period of 24 hours.</span>
            <span class="d-block"><b>Second time offenders:</b> You will not be allowed to use the office or the office resources for a period of one week.</span>
            <span class="d-block"><b>Repeat offenders:</b> At the discretion of the officers, your office privileges will be suspended for any period of time including indefinitely.</span>
            <span class="d-block">Fair warning and reason will be given prior to the ban.</span>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data () {
    return {
      // policies whose descriptions follow the same general form
      // policies with special descriptions are coded directly into the markup
      policies: [
        {
          name: 'General Policy',
          rules: [
            'Pick up after yourself.',
            'Do not leave personal items in the office (LUG is not responsible for the loss or theft of valuables).',
            'Try not to disturb others (excessive noise, etc.).',
            'Keep your hands to yourself (see Assault Policy below).',
          ],
        },
        {
          name: 'Door Policy',
          rules: [
            'The LUG Office is open anytime there is a valid keyholder present.',
            'In all other instances the doors should remain closed and locked.',
            'The last keyholder to leave is responsible for ensuring that this is the case.',
          ],
        },
        {
          name: 'Assault Policy',
          rules: [
            'Assault is defined as any offensive and intentional physical contact with another person without their consent.',
            'Violator is permanently banned from LUG and a police report will be filed.',
            'A pardon may be granted by majority vote of the executive council.',
          ],
        },
        {
          name: 'Freezer Policy',
          rules: [
            'Individuals seeking to use the freezer must seek permission from a LUG officer or council member.',
            'Organizations that seek to use the freezer to store items must seek permission from a LUG officer at least 1 week prior.',
            'Violations of this will result in items stored being thrown out and with no compensation for any items.',
          ],
        },
      ],
    };
  },
};
</script>

