/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, newColor) {
  const currColor = image[sr][sc];
  if (currColor === newColor) return image;
  const queue = [[sr, sc]];

  while (queue.length) {
    // remove the first one on queue and return it
    const [row, col] = queue.shift();
    if (image[row][col] === currColor) {
      image[row][col] = newColor;
      // if equal to currColor then push to tail of queue until all currColor transverse
      if (row - 1 >= 0) queue.push([row - 1, col]); //up
      if (row + 1 < image.length) queue.push([row + 1, col]); //down
      if (col + 1 < image[0].length) queue.push([row, col + 1]); //right
      if (col - 1 >= 0) queue.push([row, col - 1]); //left
    }
  }
  return image
};

let image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
  ],
  sr = 1,
  sc = 1,
  newColor = 2;
let res = floodFill(image, sr, sc, newColor);
console.log(res);
