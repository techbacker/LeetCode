from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.recursion(rowIndex, [1,1], 1)
    def recursion(self, rowIndex, result, times) -> List[int]:
        if rowIndex == 0:
          return result[1:]
        elif rowIndex == 1:
          return result
        elif rowIndex == times:
          return result

        tmp = []
        for i in range(len(result) - 1):
          tmp.append(result[i]+result[i+1])
        if len(tmp) > 1:
          del result[1:len(result) - 1]
        for i in range(len(tmp)):
          result.insert(i+1, tmp[i])
        times += 1
        return self.recursion(rowIndex, result, times)

print(Solution().getRow(2))
print(Solution().getRow(3))
print(Solution().getRow(4))