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
    async updateData ({ commit, dispatch }, params) {
      const officers = await dispatch('getData', params);
      commit('setData', officers);
    },
    getData ({ state }, params = {}) {
      return lugApi.getOfficers({
        isMock: !!state.useMockData,
        ...params,
      });
    },
  },
};
