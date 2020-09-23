#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] >= nums[0] and nums[mid] != nums[len(nums) - 1]:
                l = mid + 1
            elif nums[mid] <= nums[len(nums) - 1] and nums[mid] != nums[0]:
                r = mid
            else:
                r = mid
        return nums[0]
# @lc code=end

