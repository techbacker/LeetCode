#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        if len(nums) < 10:
            for i in range(left, right):
                if nums[i] == target:
                    return i

        def find(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        # find the pivot index and break them to two arrays
        for i in range(left + 1, right):
            if nums[i-1] > nums[i]:
                result_1 = find(0, i-1)
                if result_1 != -1:
                    return result_1
                result_2 = find(i, len(nums) - 1)
                if result_2 != -1:
                    return result_2
        return -1



s = Solution()
print(s.search([1,3], 3))
# @lc code=end

