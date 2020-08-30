#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        cur = x // 2
        if cur * cur == x:
            return cur
        power = 0
        while cur * cur > x:
            cur = cur // 2
        print('cur', cur)
        while power <= x:
            power = cur * cur
            cur += 1
        return cur - 2

s = Solution()
print(s.mySqrt(1))
# @lc code=end

