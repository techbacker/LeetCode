/**
 * @param {number[][]} A
 * @param {number[][]} B
 * @return {number[][]}
 */
var intervalIntersection = function (A, B) {
  let res = []
  for (let i = 0; i < A.length; i++) {
    for (let j = 0; j < B.length; j++) {
      const [aStart, aEnd] = A[i]
      const [bStart, bEnd] = B[j]
      const start = Math.max(aStart, bStart)
      const end = Math.min(aEnd, bEnd)
      if (start <= end) res.push([start,end])
      if (aEnd < bStart) continue
    }
  }
  return res
}
