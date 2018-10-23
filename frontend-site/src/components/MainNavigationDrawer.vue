<template>
  <v-navigation-drawer
    persistent
    :width="200"
    :value="value"
    @input="$emit('input', $event)"
    enable-resize-watcher
    fixed app>
    <v-container fluid class="pl-0 pr-0 pt-0">
      <v-layout row :class="{ 'site-logo pt-3': true, 'pb-3': $vuetify.breakpoint.mdAndUp, 'pb-2': $vuetify.breakpoint.smAndDown }">
        <v-flex class="text-xs-center">
          <img :src="require('@/assets/whiteTux.png')" class="mr-1"/>
          <h1 class="title">LUG@UIC</h1>
        </v-flex>
      </v-layout>
      <v-layout row>
        <v-flex>
          <!-- list of site links -->
          <v-list>
            <template v-for="(item, i) in pages">
              <v-list-tile v-if="item.to || item.href" :key="i" :to="item.to" :href="item.href">
                <v-list-tile-content>
                  <v-list-tile-title>{{ item.name }}</v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
              <v-list-group v-else :key="i">
                <v-list-tile slot="activator">
                  <v-list-tile-content>
                    <v-list-tile-title>{{ item.name }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile v-for="(subItem, j) in item.sublinks" :key="j" :to="subItem.to" :href="subItem.href">
                  <v-list-tile-content>
                    <v-list-tile-title>{{ subItem.name }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list-group>
            </template>
          </v-list>
        </v-flex>
      </v-layout>
    </v-container>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: {
    value: {
      type: Boolean,
    },
  },
  computed: {
    pages: () => [
      {
        name: 'Home',
        to: '/',
      },
      {
        name: 'Projects',
        sublinks: [
          {
            name: 'Project Listing',
            to: '/projects',
          },
          {
            name: 'Wiki',
            // TODO: eventually delete wiki page component
            // to: '/wiki',
            href: 'https://lug.cs.uic.edu/wiki/doku.php?id=start',
          },
        ],
      },
      {
        name: 'Events',
        to: '/events',
      },
      {
        name: 'Services',
        to: '/services',
      },
      {
        name: 'About',
        to: '/about',
      },
    ],
  },
};
</script>

<style lang="scss">
.site-logo {
  background-color: black;
  // same box shadow as v-toolbar
  -webkit-box-shadow: 0 2px 4px -1px rgba(0,0,0,.2), 0 4px 5px 0 rgba(0,0,0,.14), 0 1px 10px 0 rgba(0,0,0,.12);
  box-shadow: 0 2px 4px -1px rgba(0,0,0,.2), 0 4px 5px 0 rgba(0,0,0,.14), 0 1px 10px 0 rgba(0,0,0,.12);

  img {
    height: 30px;
    vertical-align: middle;
    display: inline-block;
  }

  h1 {
    font-family: monospace!important;
    display: inline-block;
    color: #0F0;
    font-size: 25px!important;
    align-self: center;
  }
}
</style>
