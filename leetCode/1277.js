/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function (matrix) {
  let m = matrix.length
  if (m == 0) return 0
  let n = matrix[0].length
  let res = 0
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] == 0) continue
      if (i == 0 || j == 0) {
        res++
        continue
      }
      let min = Math.min(
        matrix[i - 1][j],
        matrix[i][j - 1],
        matrix[i - 1][j - 1]
      );
      matrix[i][j] += min
      res += matrix[i][j]
    }
  }
  return res
}

let matrix = [
  [0, 1, 1, 1],
  [1, 1, 1, 1],
  [0, 1, 1, 1],
]

console.log(countSquares(matrix))