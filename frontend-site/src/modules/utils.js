export function isDebugMode () {
  // this parameter is only defined when using the dev server from the npm run serve command
  return window.webpackHotUpdate !== undefined;
}

// check if 2 arrays have equivalent values; compareFn compares 2 items and returns true if 2 inputs are equivalent, false otherwiase
export function arraysAreEquivalent (arr1 = [], arr2 = [], compareFn = (a, b) => a === b) {
  return arr1.every(a => arr2.some(b => compareFn(a, b))) &&
    arr2.every(a => arr1.some(b => compareFn(a, b)));
}
