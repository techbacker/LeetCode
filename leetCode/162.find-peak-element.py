#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # iteration
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left

        # recursion version
        # def search(nums, l, r):
        #     if l == r:
        #         return l
        #     mid = (l + r) // 2
        #     if nums[mid] < nums[mid+1]:
        #         return search(nums, mid + 1, r)
        #     else:
        #         return search(nums, l, mid)
        # return search(nums, 0, len(nums) - 1)
# @lc code=end

