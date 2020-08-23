/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  // declare the array to store the course we have to take
  let inDegree = new Array(numCourses).fill(0);
  let count = 0;
  // care about which course has prerequisites
  for (let i = 0; i < prerequisites.length; i++) {
    inDegree[prerequisites[i][0]]++;
  }

  // declare the stack and put the course we can take now
  let stack = [];
  for (let i = 0; i < inDegree.length; i++) {
    if (inDegree[i] == 0) {
      stack.push(i);
    }
  }
  // loop when the stack is not empty
  // count += 1 every time we iterate here
  // if the prerequisites equal to current value then the element on inDegree--
  // if the prerequisites == 0 then put the course into stack
  while (stack.length != 0) {
    count++;
    let curr = stack.pop();
    for (let i = 0; i < prerequisites.length; i++) {
      if (prerequisites[i][1] == curr) {
        inDegree[prerequisites[i][0]]--;
        if (inDegree[prerequisites[i][0]] == 0) {
          stack.push(prerequisites[i][0]);
        }
      }
    }
  }
  // return whether num of course is equal to count
  return numCourses == count;
};
