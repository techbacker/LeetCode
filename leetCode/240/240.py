class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        col_middle  = len(matrix[0]) // 2
        row = 0
        if len(matrix) <= 1 or len(matrix[0]) <= 1:
            for i in matrix:
                for j in i:
                    if j is target:
                        return True
            return False

        while len(matrix) > 1 and matrix[row][col_middle] < target and row < len(matrix) - 1:
            row += 1

        for i in range(len(matrix)):
            for j in range(0, col_middle):
                if matrix[i][j] is target:
                    return True

        for i in range(0, row + 1):
            for j in range(col_middle, len(matrix[0])):
                if matrix[i][j] is target:
                    return True
        return False

res = Solution().searchMatrix([[48,65,70,113,133,163,170,216,298,389],[89,169,215,222,250,348,379,426,469,554],[178,202,253,294,367,392,428,434,499,651],[257,276,284,332,380,470,516,561,657,698],[275,331,391,432,500,595,602,673,758,783],[357,365,412,450,556,642,690,752,801,887],[359,451,534,609,654,662,693,766,803,964],[390,484,614,669,684,711,767,804,857,1055],[400,515,683,732,812,834,880,930,1012,1130],[480,538,695,751,864,939,966,1027,1089,1224]],
642)
print(res)
print(Solution().searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))
print(Solution().searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 20))