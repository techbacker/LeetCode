/**
 * @param {number[][]} points
 * @param {number} K
 * @return {number[][]}
 */
var kClosest = function (points, K) {
  let result = []
  let longestIndex = 0
  for (let i = 0; i < points.length; i++) {
      let distance = Math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1])
      if (i < K) {
        result.push({
          index: i,
          distance,
          value: points[i]
        })
        if (distance > result[longestIndex].distance) {
          longestIndex = i
        }
        continue
      }
      // check current distance compare with largest one
      if (distance < result[longestIndex].distance) {
        result.splice(longestIndex, 1)
        result.push({
          index: i,
          distance,
          value: points[i]
        })
        for (let i in result) {
          if (result[i].distance > result[longestIndex].distance) {
            longestIndex = i
          }
        }
    }
  }
  return result.map((i) => i.value)
}

console.log(
  kClosest(
    [
      [3, 3],
      [5, -1],
      [-2, 4],
    ],
    2
  )
)
console.log(
  kClosest(
    [
      [68, 97],
      [34, -84],
      [60, 100],
      [2, 31],
      [-27, -38],
      [-73, -74],
      [-55, -39],
      [62, 91],
      [62, 92],
      [-57, -67],
    ],
    5
  )
)