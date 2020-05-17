/**
 * @param {number[]} A
 * @return {number}
 */
var maxSubarraySumCircular = function (A) {
  if (A == null || A.length == 0) return 0
  let maxTillHere = A[0],
    maxInTotal = A[0],
    minTillHere = A[0],
    minInTotal = A[0],
    sum = A[0]

  for (let i = 1; i < A.length; i++) {
    maxTillHere = maxTillHere + A[i] > A[i] ? maxTillHere + A[i] : A[i]
    maxInTotal = Math.max(maxTillHere, maxInTotal)
    minTillHere = minTillHere + A[i] < A[i] ? minTillHere + A[i] : A[i]
    minInTotal = Math.min(minTillHere, minInTotal)
    sum += A[i]
  }

  // all elements are negative
  if (minInTotal === sum) return maxInTotal
  return Math.max(sum - minInTotal, maxInTotal)
}

let res = maxSubarraySumCircular([5, -3, 5])
console.log(res)