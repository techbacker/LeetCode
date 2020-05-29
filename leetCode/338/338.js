/**
 * @param {number} num
 * @return {number[]}
 */
var recursion = function (num, power, currentSet, result) {
  if (result.length === num + 1) {
    return result
  }
  let elementsToPush = Math.pow(2, power)
  for (let i = 0; i < elementsToPush; i++) {
    // edge case
    if (currentSet[i] === 0) {
      result.push(1)
      continue
    }
    // less than current set => just put my current set value
    if (i < currentSet.length) {
      result.push(currentSet[i])
    } else {
      result.push(currentSet[i - currentSet.length] + 1)
    }
    if (result.length === num + 1) {
      return result
    }
  }
  currentSet = result.slice(result.length - elementsToPush, result.length)
  recursion(num, power+1, currentSet, result)
  return result
}

var countBits = function (num) {
  return recursion(num, 0, [0], [0])
}

console.log(countBits(5))
console.log(countBits(10))