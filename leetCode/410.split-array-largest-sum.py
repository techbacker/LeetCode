#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
from typing import List
# @lc code=start
class Solution:
    ### check if mid can be maxium subarray sum
    def check(self, mid, array, n, K):
        count = 0
        sum = 0
        for i in range(n):

            # If individual element is greater
            # maximum possible sum
            if (array[i] > mid):
                return False

            # Increase sum of current sub - array
            sum += array[i]

            # If the sum is greater than
            # mid increase count
            if (sum > mid):
                count += 1
                sum = array[i]
        count += 1
        # Check condition
        if (count <= K):
            return True
        return False

    def splitArray(self, nums: List[int], m: int) -> int:
        start = 1
        end = 0
        answer = 0
        n = len(nums)

        for i in range(n):
            end += nums[i]

        while (start <= end):
            mid = (start + end) // 2
            if (self.check(mid, nums, n, m)):
                answer = mid
                end = mid - 1
            else:
                start = mid + 1

        return answer


s = Solution()
s.splitArray([1,2,3,4,5], 2)
s.splitArray([1,4,4], 3)
s.splitArray([7,2,5,10,8], 2)
s.splitArray([1,2,3,4,5], 1)
s.splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8], 8)

# @lc code=end

