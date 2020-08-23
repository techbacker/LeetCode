/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
  let maxInd = Math.max(...candies)
  return candies.map((it) => it + extraCandies >= maxInd)
}

let res = kidsWithCandies([4,1,4,8,9,6,4], 1)
console.log(res)