import { mockOfficers, mockEvents } from '@/modules/mockData';

export class LugApi {
  constructor (baseUrl = '') {
    this._baseUrl = baseUrl;
  }

  generateUrl (path = '') {
    return [this._baseUrl, path].join('');
  }

  _getJson (url = '') {
    return fetch(url).then(res => res.json());
  }

  // warn developers that mock data is being returned
  _checkParamsForMock (params) {
    if (typeof params === 'object' && params.isMock) {
      console.warn('using mock data for API call');
    }
  }

  async getOfficers (params = {}) {
    this._checkParamsForMock(params);
    // TODO: error checking for semester?
    const apiUrl = `/api/officers${params.semester ? `?semester=${params.semester}` : ''}`;
    return !params.isMock
      ? this._getJson(this.generateUrl(apiUrl))
      : Promise.resolve(mockOfficers);
  }

  async getEvents (params = {}) {
    this._checkParamsForMock(params);
    return !params.isMock
      ? this._getJson(this.generateUrl('/api/events'))
      : Promise.resolve(mockEvents);
  }
}

export default new LugApi(window.webpackHotUpdate !== undefined ? 'http://localhost:5000' : '');
