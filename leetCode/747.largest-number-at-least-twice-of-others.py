#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#
from typing import List
# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_num_index = 0

        if len(nums) == 1:
            return largest_num_index

        def findLargestIndex(nums):
            nonlocal largest_num_index
            for i in range(0, len(nums)):
                if nums[i] > nums[largest_num_index]:
                    largest_num_index = i
        findLargestIndex(nums)

        for i in range(0, len(nums)):
            if i != largest_num_index and nums[largest_num_index] // 2 < nums[i]:
                return -1

        return largest_num_index
# @lc code=end
s = Solution()
# res = s.dominantIndex([3, 6, 1, 0])
# res1 = s.dominantIndex([1])
res2 = s.dominantIndex([0,1,1,2])
print(res2)