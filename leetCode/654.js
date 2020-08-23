/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */

var findMaxIndex = function (arr, startIndex, endIndex) {
  let maxIndex = startIndex;
  for (let i = startIndex; i < endIndex; i++) {
    if (arr[maxIndex] < arr[i]) {
      maxIndex = i;
    }
  }
  return maxIndex;
};

var helper = function (nums, startInd, endInd) {
  if (startInd === endInd) return null;
  let maxIndex = findMaxIndex(nums, startInd, endInd);
  // max value equals to root
  let root = new TreeNode(nums[maxIndex]);
  root.left = helper(nums, startInd, maxIndex);
  root.right = helper(nums, maxIndex + 1, endInd);
  return root;
};

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var constructMaximumBinaryTree = function (nums) {
  return helper(nums, 0, nums.length);
};
