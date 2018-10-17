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
    async updateEventData ({ dispatch, state }) {
      const data = await lugApi.getEvents({ isMock: !!state.useMockData });
      dispatch('setEventData', data);
    },
  },
};
