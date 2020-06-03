class Solution:
    cache =  {}
    def climbStairs(self, n: int) -> int:
      def rec_climb_stairs(n):
        if n in self.cache:
          return self.cache[n]
        if n < 3:
          return n
        else:
          result = rec_climb_stairs(n-1) + rec_climb_stairs(n-2)
        self.cache[n] = result
        return result

      return rec_climb_stairs(n)

print(Solution().climbStairs(6))
print(Solution().climbStairs(5))
print(Solution().climbStairs(4))
print(Solution().climbStairs(3))
print(Solution().climbStairs(2))