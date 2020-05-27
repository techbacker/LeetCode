/**
 * @param {number} N
 * @param {number[][]} dislikes
 * @return {boolean}
 */
var dfs = function (colors, color, node, hatersMap) {
  if (colors[node] != 0) {
    return colors[node] === color
  }
  colors[node] = color
  if (hatersMap.has(node)) return true;
  for (let i in hatersMap.get(node)) {
    if (!dfs(colors, -color, hatersMap.get(node)[i], hatersMap)) return false
  }
  return true
}

var possibleBipartition = function (N, dislikes) {
  // build a graph
  // try to color each node
  // 0. if the node hasn't been color => color 1
  // 1. color its dislike nodes to -color => color -1
  // check conflict => false
  let hatersMap = new Map()
  for (let i in dislikes) {
    let a = dislikes[i][0]
    let b = dislikes[i][1]
    if (!hatersMap.has(a)) {
      hatersMap.set(a, [])
    }
    if (!hatersMap.has(b)) {
      hatersMap.set(b, [])
    }
    hatersMap.get(a).push(b)
    hatersMap.get(b).push(a)
  }
  let colors = new Array(N+1).fill(0)
  for (let i = 1; i <= N; i++) {
    if (colors[i] == 0 && !dfs(colors, 1, i, hatersMap)) return false
  }
  return true
};

console.log(
  possibleBipartition(3,[
    [1, 2],
    [1, 3],
    [2, 3],
  ])
);