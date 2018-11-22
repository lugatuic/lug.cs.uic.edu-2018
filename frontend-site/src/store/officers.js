import lugApi from '@/modules/LugApi';

export default {
  namespaced: true,
  state: {
    // TODO: should we cache officer list, and if so, for how long or when should it refresh?
    // data: [],
    useMockData: false,
  },
  mutations: {
    setData (state, data) {
      if (!Array.isArray(data)) {
        throw new Error(`New data is not an array: ${JSON.stringify(data)}`);
      }
      state.data = data;
    },
  },
  getters: {
    currentSemester () {
      const currentDate = new Date();
      const currentMonth = currentDate.getMonth() + 1; // getMonth is 0 indexed, so add 1
      const currentYear = currentDate.getUTCFullYear();
      let currentSemester = '';
      if (currentMonth <= 5) { // up to May
        currentSemester = 'SPRING';
      } else if (currentMonth <= 8) { // up to August
        currentSemester = 'SUMMER';
      } else {
        currentSemester = 'FALL';
      }
      return `${currentSemester}_${currentYear}`;
    },
  },
  actions: {
    async updateData ({ commit, dispatch }, params) {
      const officers = await dispatch('getData', params);
      commit('setData', officers);
      return officers;
    },
    getData ({ state }, params = {}) {
      return lugApi.getOfficers({
        isMock: !!state.useMockData,
        ...params,
      });
    },
  },
};
