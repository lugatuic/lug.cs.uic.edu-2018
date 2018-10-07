import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    useLightTheme: false,
  },
  mutations: {
    toggleLightTheme (state, newValue) {
      state.useLightTheme = (newValue !== undefined) ? !!newValue : !state.useLightTheme;
    },
  },
  actions: {

  },
});
