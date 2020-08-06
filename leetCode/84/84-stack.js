/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function (heights) {
  let stack = [];
  stack.push(-1);
  let maxArea = 0;

  for (let i = 0; i < heights.length; i++) {
    while (
      stack[stack.length - 1] != -1 &&
      heights[stack[stack.length - 1]] >= heights[i]
    ) {
      const top = stack[stack.length - 1];
      maxArea = Math.max(
        maxArea,
        heights[stack.pop()] * (i - stack[stack.length - 1] - 1)
      );
    }
    stack.push(i);
  }

  while (stack[stack.length - 1] != -1) {
    const pop = stack.pop();
    maxArea = Math.max(
      maxArea,
      heights[pop] * (heights.length - 1 - stack[stack.length - 1])
    );
  }
  return maxArea;
};
