import lugApi from '@/modules/LugApi';

export default {
  namespaced: true,
  state: {
    data: [],
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
  actions: {
    async updateData ({ commit, state }) {
      const data = await lugApi.getEvents({ isMock: !!state.useMockData });
      // send data sorted by start date
      commit('setData', data.slice().sort((a, b) => new Date(a.timeStart) - new Date(b.timeStart)));
    },
  },
};
