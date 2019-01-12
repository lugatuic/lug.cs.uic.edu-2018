import Vue from 'vue';
import Vuex from 'vuex';
import events from './events';
import officers from './officers';
import projects from './projects';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    events,
    officers,
    projects,
  },
  state: {
    useLightTheme: false,
  },
  mutations: {
    toggleLightTheme (state, newValue) {
      state.useLightTheme = (newValue !== undefined) ? !!newValue : !state.useLightTheme;
    },
  },
  strict: true,
});
