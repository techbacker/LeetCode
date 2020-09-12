#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
import math
from typing import List

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binary_search(x):
            # binary search the pos, the insertion order
            l, r = 0, len(arr)-1
            while(l <= r):
                mid = l + (r-l)//2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    l = mid+1
                else:
                    r = mid-1
            return r

        # find the x in the arr
        index = binary_search(x)
        left, right = index, index + 1
        result = []
        count = 0
        while count < k:
            left_diff = left >= 0 and right < len(arr) and abs(x - arr[left]) <= abs(arr[right] - x)
            right_diff = left >= 0 and right < len(arr) and abs(x - arr[left]) > abs(arr[right] - x)

            if right >= len(arr) or left_diff:
                result.insert(0, arr[left])
                left -= 1
            elif left < 0 or right_diff:
                result.append(arr[right])
                right += 1
            count += 1
        return result

s = Solution()
# print(s.findClosestElements([1,2,3,4,5], 4, -1))
print(s.findClosestElements([1,2,3,4,5], 4, 3))
# @lc code=end

