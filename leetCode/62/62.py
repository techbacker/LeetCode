class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for col in range(m)] for row in range(n)]
        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                    continue
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[i][j]

        return res

print(Solution().uniquePaths(3,2))
print(Solution().uniquePaths(3,3))
print(Solution().uniquePaths(3,6))
print(Solution().uniquePaths(7,3))