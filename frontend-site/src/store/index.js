import Vue from 'vue';
import Vuex from 'vuex';
import events from './events';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    events,
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
