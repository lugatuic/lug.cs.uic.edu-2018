import lugApi from '@/modules/LugApi';

export default {
  namespaced: true,
  state: {
    data: [],
    // TODO: remove mock parameter once backend has API ready
    useMockData: true,
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
      const data = await lugApi.getOfficers({ isMock: !!state.useMockData });
      // TODO: sort by rank?
      commit('setData', data);
    },
  },
};
