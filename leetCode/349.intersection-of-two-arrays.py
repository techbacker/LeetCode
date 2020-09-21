#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(nums, target):
            left, right = 0 , len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def find_and_append(longerArr, shortArr):
            for value in longerArr:
                intersection = -1
                if dictionary.get(value) is None:
                    intersection = binary_search(shortArr, value)
                    if value ==  6:
                        print(intersection)
                    if intersection != -1:
                        result.append(shortArr[intersection])
                        dictionary[value] = True
                else:
                    continue

        result = []
        dictionary = {}
        nums1.sort()
        nums2.sort()
        if len(nums1) >= len(nums2):
            find_and_append(nums1, nums2)
        else:
            find_and_append(nums2, nums1)

        return result
# @lc code=end

