/* 
  1282. Group the People Given the Group Size They Belong To
  There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.
  You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution.
  
  Example 1:
  Input: groupSizes = [3,3,3,3,3,1,3]
  Output: [[5],[0,1,2],[3,4,6]]
  Explanation: 
  Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
  
  Example 2:
  Input: groupSizes = [2,1,3,3,3,2]
  Output: [[1],[0,5],[2,3,4]]
  
  Constraints:
  groupSizes.length == n
  1 <= n <= 500
  1 <= groupSizes[i] <= n
*/

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