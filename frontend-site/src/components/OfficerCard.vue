<template>
  <v-card class="officer-card">
    <v-img
      contain
      :src="avatarUrl"
      aspect-ratio="2.75"/>
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
  computed: {
    avatarUrl () {
      return this.officer.image || require('@/assets/whiteTux.png');
    },
  },
};
</script>

// <div class="col-md-3" id="StephenWalden">
//     <div class="card card-01">
//       <div class="profile-box">
//           <img class="card-img-top rounded-circle" alt="Card image cap" src="./avatar.jpg">
//       </div>
//       <div class="card-body text-center">
//         <h4 class="card-title">Stephen Walden</h4>
//         <p class="card-text">I started coding with computer related video games. I have been developing simple command line interfaces since the age of 14, and have been working on learning about technology ever since that time. Lately I have been working on several different items. You can see a sample of what I have been working on if you visit my website.</p>
//         <span class="social-box">
//             <a id="fb" href="https://www.facebook.com/stephen.walden.100" target="_blank"><i class="fa fa-facebook"></i></a>
//             <a class="hidden" id="tw" href="#" target="_blank"><i class="fa fa-twitter"></i></a>
//             <a class="hidden" id="gp" href="#" target="_blank"><i class="fa fa-google-plus"></i></a>
//             <a id="li" href="https://www.linkedin.com/in/stephen-3-walden" target="_blank"><i class="fa fa-linkedin"></i></a>
//             <a id="lk" href="https://walden1995.github.io/" target="_blank"><i class="fa fa-external-link-square"></i></a>
//         </span>
//       </div>
//     </div>
//   </div>
