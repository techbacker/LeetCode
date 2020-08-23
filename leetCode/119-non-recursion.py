from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []

        prev_row = [1]
        for i in range(0,rowIndex):
            row = [1]
            for j in range(1,i+1):
                row.append(prev_row[j-1] + prev_row[j])

            row.append(1)
            prev_row = row

        return prev_row

print(Solution().getRow(3))