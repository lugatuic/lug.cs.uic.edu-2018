<template>
  <v-app>
    <v-navigation-drawer
      persistent
      v-model="showNavDrawer"
      enable-resize-watcher
      fixed app>
      the nav drawer
      <!-- <v-list>
        <v-list-tile
          value="true"
          v-for="(item, i) in items"
          :key="i"
        >
          <v-list-tile-action>
            <v-icon v-html="item.icon"></v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title v-text="item.title"></v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list> -->
    </v-navigation-drawer>
    <main-app-bar @sidemenu-button-click="showNavDrawer = !showNavDrawer"/>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import MainAppBar from '@/components/MainAppBar';

export default {
  name: 'App',
  components: {
    MainAppBar,
  },
  data () {
    return {
      showNavDrawer: true,
    };
  },
};
</script>
