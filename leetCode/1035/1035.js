/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
var maxUncrossedLines = function (a, b) {
  let result = 0
  let dp = [[a + 1][b + 1]]
  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      if (a[i] === b[j]) {
        dp[i][j] = 1 + dp[i - 1][j - 1]
      } else {
        dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j])
      }
    }
  }
  return dp[a.length][b.length]
}

console.log(maxUncrossedLines([1,4,2], [1,2,4]))
