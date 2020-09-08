#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [None] * 2

        def findStartIndex(nums, target):
            index = -1
            start, end = 0, len(nums) - 1

            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1

                if nums[mid] == target:
                    index = mid
            return index

        def findEndIndex(nums, target):
            index = -1
            start, end = 0, len(nums) - 1

            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
                if nums[mid] == target:
                    index = mid
            return index

        result[0] = findStartIndex(nums, target)
        result[1] = findEndIndex(nums, target)
        return result
# @lc code=end

