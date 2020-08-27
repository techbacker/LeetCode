#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        integer = int(''.join(map(str, digits)))
        integer += 1
        for i in str(integer):
            res.append(int(i))
        return res
# @lc code=end

s = Solution()
res = s.plusOne([1,2,3])
print(res)