class Solution:
    cache = {}
    def fib(self, N: int) -> int:
      def rec_fib(N) -> int:
        if N in self.cache:
          return self.cache[N]
        if N < 2:
          result = N
        else:
          result = rec_fib(N-1) + rec_fib(N-2)
        self.cache[N] = result
        return result

      return rec_fib(N)

print(Solution().fib(20))