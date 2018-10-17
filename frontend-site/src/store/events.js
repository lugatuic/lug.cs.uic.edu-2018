import lugApi from '@/modules/LugApi';

export default {
  namespaced: true,
  state: {
    eventData: [],
    // TODO: remove mock parameter once backend has API ready
    useMockData: true,
  },
  mutations: {
    setEventData (state, data) {
      if (!Array.isArray(data)) {
        throw new Error(`New event data is not an array: ${JSON.stringify(data)}`);
      }
      state.eventData = data;
    },
  },
  actions: {
    async updateEventData ({ commit, state }) {
      const data = await lugApi.getEvents({ isMock: !!state.useMockData });
      // send data sorted by start date
      commit('setEventData', data.slice().sort((a, b) => new Date(a.timeStart) - new Date(b.timeStart)));
    },
  },
};
