class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        res = False
        for i in range(row):
            res = res or self.binarySearch(matrix[i], target)
        return res

    def binarySearch(self, row, target):
        start, end = 0, len(row) - 1
        while start <= end:
            mid = (start + end) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False

print(Solution().searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))