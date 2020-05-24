/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  let boolean = false
  let charPointMap = new Map()
  let accumulateCharPointAt = 0

  for (let i = s1.length - 1; i >= 0; i--) {
    accumulateCharPointAt += s1.codePointAt(i)
  }

  for (let j = 0; j < s2.length; j++) {
    if (s1.includes(s2[j]) && s2.length >= s1.length) {
      let subArray = s2.slice(j, j + s1.length)
      let charPointOfSubArray = 0
      if (subArray.includes(s1)) return true
      for (let k = s1.length - 1; k >= 0; k--) {
        if (!subArray.includes(s1[k])) break
        charPointOfSubArray += subArray.codePointAt(k)
      }
      if (charPointOfSubArray === accumulateCharPointAt) {
        return true;
      }
    }
  }
  return boolean;
};

console.log(checkInclusion("abc", "bbbca")); // expected: true
console.log(checkInclusion("horse", "ros")); // expected: false
console.log(checkInclusion("ab", "ba")); // expected: true
console.log(checkInclusion("ab", "eidboaoo")); // expected: false
