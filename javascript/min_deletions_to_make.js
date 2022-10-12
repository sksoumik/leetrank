// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function (s) {
  let charFrequency = new Map(),
    used = new Set(),
    res = 0;

  //Iterate through all the characters & store the char along with frequency in map
  for (const char of s) {
    //If the character is already present in map, increment the frequency
    if (charFrequency.has(char))
      charFrequency.set(char, charFrequency.get(char) + 1);
    //If the character is not present, add it to map with frequency set to 1
    else charFrequency.set(char, 1);
  }

  //Now iterate through the Map created in above steps
  for (let [char, freq] of charFrequency.entries()) {
    //Check if the frequency is already present for any other character, 
    //decrement the frequency till it reaches either a frequency which 
    //is not used already or 0 (because if frequency reaches 0 the character is no more present)
    //Meanwhile increment the 'res', so we will get to know the count of deletions required
    while (used.has(freq) && freq > 0) {
      freq--;
      res++;
    }

    //Add the frequency to the set 'used', 
    //so for the next characters we can check the already used frequency
    used.add(freq);
  }
  return res;
};
