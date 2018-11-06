import { mockOfficers, mockEvents } from '@/modules/mockData';
import { isDebugMode } from '@/modules/utils';

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
  _checkParamsForMock (params, url) {
    if (typeof params === 'object' && params.isMock) {
      console.warn('using mock data for API call', url);
    }
  }

  async getOfficers (params = {}) {
    // TODO: error checking for semester or leave it server side (i.e. server returns 4xx error)?
    const apiUrl = `/api/officers${params.semester ? `?semester=${params.semester}` : ''}`;
    this._checkParamsForMock(params, apiUrl);
    return !params.isMock
      ? this._getJson(this.generateUrl(apiUrl))
      : Promise.resolve(mockOfficers);
  }

  async getEvents (params = {}) {
    const apiUrl = '/api/events';
    this._checkParamsForMock(params, apiUrl);
    return !params.isMock
      ? this._getJson(this.generateUrl(apiUrl))
      : Promise.resolve(mockEvents);
  }
}

// use localhost for dev purposes, current domain for production
export default new LugApi(isDebugMode() ? 'http://localhost:5000' : '');
