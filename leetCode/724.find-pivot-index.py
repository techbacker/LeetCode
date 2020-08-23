#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
from typing import List

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum, left_sum = 0, 0
        for i in nums:
            sum += i
        for i in range(0, len(nums)):
            if left_sum == sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1
# @lc code=end
s = Solution()
res = s.pivotIndex([1,7,3,6,5,6])
print(res)