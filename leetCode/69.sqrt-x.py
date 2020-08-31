#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        def binary_serach(x) -> int:
            if x < 2:
                return x
            left, right = 0, x // 2

            while left <= right:
                pivot = left + (right - left) // 2
                num = pivot * pivot
                if num == x:
                    return pivot
                elif num < x:
                    left = pivot + 1
                elif num > x:
                    right = pivot - 1

            return right
        return binary_serach(x)
s = Solution()
print(s.mySqrt(30))
# @lc code=end

