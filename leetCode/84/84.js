/**
 * @param {number[]} heights
 * @return {number}
 */

function findMinIndex (heights, start, end) {
    let res = start
    for (let i = start; i <= end; i++) {
        if (heights[res] > heights[i]) {
            res = i
        }
    }
    return res
}

function helper (heights, start, end) {
    if (start > end)
        return 0
    let minInd = findMinIndex(heights, start, end)
    return Math.max(heights[minInd] *  (end - start + 1), helper(heights, start, minInd - 1), helper(heights, minInd + 1, end))
};

var largestRectangleArea = function(heights) {
    return helper(heights, 0, heights.length - 1)
};