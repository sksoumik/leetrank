// https://leetcode.com/problems/excel-sheet-column-number
// Given a string columnTitle that represents the column title as appear in an Excel sheet,
// return its corresponding column number.

// A -> 1
// B -> 2
// C -> 3
// ...
// Z -> 26
// AA -> 27
// AB -> 28

/**
 * @param {string} columnTitle
 * @return {number}
 */
// video explanation: https://youtu.be/DQKafgIBeyI

var titleToNumber = function (columnTitle) {
  let multiplier = 1;
  let column = 0;
  for (let i = columnTitle.length - 1; i >= 0; i--) {
    column += (columnTitle.charCodeAt(i) - 64) * multiplier;
    multiplier *= 26;
  }
  return column;
};

console.log(titleToNumber("A"));
console.log(titleToNumber("AB"));
console.log(titleToNumber("ZY"));
