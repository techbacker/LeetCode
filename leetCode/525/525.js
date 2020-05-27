/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function (nums) {
  let longestSubArray = 0
  let sum = 0
  let sumMap = new Map()
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i] === 0 ? -1 : nums[i]
    if (sum === 0) {
      longestSubArray = i + 1
    } else if (!sumMap.has(sum)) {
      sumMap.set(sum, i)
    } else {
      let compareValue = i - sumMap.get(sum)
      if (longestSubArray < compareValue)
        longestSubArray = compareValue
    }
  }
  return longestSubArray
};