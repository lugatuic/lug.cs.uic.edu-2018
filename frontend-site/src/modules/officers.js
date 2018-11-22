// based on ordering in server.py
export const positionOrder = Object.freeze([
  'PRESIDENT',
  'VICE_PRESIDENT',
  'TREASURER',
  'SECRETARY',
  'TECHNICAL_OFFICER',
  'MEMBER',
]);

// converts a given semester to the date of the first month of the term
export function convertSemesterToMonthStart (semester = 'FALL_2018') {
  const [term, year] = semester.split('_');
  let month;
  if (term === 'SPRING') {
    month = 'January';
  } else if (term === 'SUMMER') {
    month = 'June';
  } else {
    month = 'September';
  }

  // first of the month
  // not 100% accurate, but good enough for simple sorting/comparison purposes
  return new Date(`${month} 1 ${year}`);
}

export function getNextSemester (semester = 'FALL_2018') {
  const [term, year] = semester.split('_');
  let nextTerm;
  if (term === 'FALL') {
    nextTerm = 'SPRING';
  } else if (nextTerm === 'SPRING') {
    nextTerm = 'SUMMER';
  } else {
    nextTerm = 'FALL';
  }

  return [
    nextTerm,
    term === 'FALL' ? (+year + 1) : year
  ].join('_');
}

export function getCurrentSemester () {
  const currentDate = new Date();
  const currentMonth = currentDate.getMonth() + 1; // getMonth is 0 indexed, so add 1
  const currentYear = currentDate.getUTCFullYear();
  let currentSemester = '';
  if (currentMonth <= 5) { // up to May
    currentSemester = 'SPRING';
  } else if (currentMonth <= 8) { // up to August
    currentSemester = 'SUMMER';
  } else {
    currentSemester = 'FALL';
  }
  return `${currentSemester}_${currentYear}`;
}
