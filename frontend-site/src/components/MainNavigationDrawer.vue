<template>
  <v-navigation-drawer
    persistent
    :value="value"
    @input="$emit('input', $event)"
    enable-resize-watcher
    fixed app>
    <v-container fluid class="pl-0 pr-0">
      <v-layout row class="site-logo">
        <v-flex class="text-xs-center">
          <img :src="require('@/assets/whiteTux.png')" class="mr-1"/>
          <h1 class="title">LUG@UIC</h1>
        </v-flex>
      </v-layout>
      <v-layout row>
        <v-flex>
          <v-divider class="mt-2"/>
        </v-flex>
      </v-layout>
      <v-layout row>
        <v-flex>
          <v-list>
            <template v-for="(item, i) in pages">
              <v-list-tile v-if="item.to" :key="i" :to="item.to">
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
                <v-list-tile v-for="(subItem, j) in item.sublinks" :key="j" :to="subItem.to">
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
            to: '/wiki',
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
  .layout {
    align-items: center;
  }
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
