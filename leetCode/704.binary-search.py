#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1

# @lc code=end
s = Solution()
res = s.search([-1, 0, 3, 5, 9, 12])
print(res)
