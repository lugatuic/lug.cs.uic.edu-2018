<template>
  <v-app :dark="!useLightTheme">
    <main-nav-drawer v-model="showNavDrawer"/>
    <main-app-bar @sidemenu-button-click="showNavDrawer = !showNavDrawer"/>
    <v-content>
      <v-fade-transition mode="out-in">
        <router-view/>
      </v-fade-transition>
    </v-content>
  </v-app>
</template>

<script>
import { mapState } from 'vuex';
import MainAppBar from '@/components/MainAppBar';
import MainNavDrawer from '@/components/MainNavigationDrawer';

export default {
  name: 'App',
  components: {
    MainAppBar,
    MainNavDrawer,
  },
  computed: {
    ...mapState(['useLightTheme']),
  },
  data () {
    return {
      showNavDrawer: false,
    };
  },
};
</script>

<style lang="scss">
.flex-container {
  display: flex;

  &.align-items-center {
    align-items: center;
  }
}

html {
  overflow-y: auto;
}

.theme--dark {
  --card-default-background-color: #424242;
  --card-default-background-color--darken-1: #212121; /* grey darken-4 */
}

.theme--light {
  --card-default-background-color: #fff;
  --card-default-background-color--darken-1: #f5f5f5; /* grey lighten-4 */
}
</style>
