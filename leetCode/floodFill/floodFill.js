/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, newColor) {
  const currColor = image[sr][sc];
  if (newColor === currColor) return image;

  function transverse(img, row, col) {
    if (row >= img.length || col >= img[0].length || row < 0 || col < 0 || img[row][col] !== currColor) {
      return;
    }
    img[row][col] = newColor
    transverse(img, row - 1, col) // up
    transverse(img, row, col + 1) // right
    transverse(img, row + 1, col) // down
    transverse(img, row, col - 1) // left
    return img
  }

  return transverse(image, sr, sc);
}

let image = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1],
], sr = 1, sc = 1, newColor = 2
let res = floodFill(image, sr, sc, newColor)
console.log(res)