/**
 * @param {number[]} groupSizes
 * @return {number[][]}
 */
var loop = function(groupSizes, i, length, result, uniqueItem) {
  if (i > length - 1) {
    return result
  }
  if (!uniqueItem[groupSizes[i]]) {
    uniqueItem[groupSizes[i]] = {
      currentInd: 0,
      currentResultInd: result.length
    }
    result.push([i])
  } else {
    // update the index on sub array
    uniqueItem[groupSizes[i]]["currentInd"] = uniqueItem[groupSizes[i]]["currentInd"] + 1
    if (uniqueItem[groupSizes[i]]["currentInd"] % groupSizes[i] !== 0) {
      // when not the first time to insert sub-array, find the existing sub array to insert
      result[uniqueItem[groupSizes[i]]["currentResultInd"]].push(i)
    } else {
      // when create new sub array to insert item
      uniqueItem[groupSizes[i]]["currentResultInd"] = result.length
      result.push([i])
    }
  }
  i += 1
  loop(groupSizes, i, length, result, uniqueItem)
}

var groupThePeople = function(groupSizes) {
  let res = []
  let uniqueItem = {}
  loop(groupSizes, 0, groupSizes.length, res, uniqueItem)
  return res
}