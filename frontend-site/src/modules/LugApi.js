import { mockOfficers, mockEvents, mockProjects } from '@/modules/mockData';
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

  _objectToUrlParams (params = {}) {
    // assumption: each value is a string or easily converted into a string
    return Object.keys(params)
      .map(key => `${key}=${params[key]}`)
      .join('&');
  }

  _toApiUrl (url = '', params = {}) {
    return [
      url,
      this._objectToUrlParams(params),
    ].filter(v => v) // filter out empty strings
    .join('?');
  }

  _defaultApiGet (baseApiUrl = '/api/someendpoint', params = {}, mockResult) {
    const apiUrl = this._toApiUrl(baseApiUrl, params);
    this._checkParamsForMock(params, apiUrl);
    return !params.isMock ?
      this._getJson(this.generateUrl(apiUrl)) :
      Promise.resolve(mockResult);
  }

  async getOfficers (params = {}) {
    // TODO: error checking for semester or leave it server side (i.e. server returns 4xx error)?
    return this._defaultApiGet('/api/officers', params, mockOfficers);
  }

  async getEvents (params = {}) {
    return this._defaultApiGet('/api/events', params, mockEvents);
  }

  async getProjects (params = {}) {
    return this._defaultApiGet('/api/projects', params, mockProjects);
  }
}

// use localhost for dev purposes, current domain for production
// TODO: make dev url and port configurable?
export default new LugApi(isDebugMode() ? 'http://localhost:5000' : '');
