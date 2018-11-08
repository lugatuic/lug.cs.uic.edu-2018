export function isDebugMode () {
  // this parameter is only defined when using the dev server from the npm run serve command
  return window.webpackHotUpdate !== undefined;
}
