class Solution:
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.myPowRecur(x, -n)
        return self.myPowRecur(x, n)

    def myPowRecur(self, x, n):
        # Base case.
        if n == 0:
            return 1

        if n % 2 == 0:
            return self.myPowRecur(x * x, int(n / 2))
        # else:
        return x * self.myPowRecur(x * x, int(n / 2))

# print(Solution().myPow(2.1, 3))
# print(Solution().myPow(1.00001, 123456))
# print(Solution().myPow(2.00000, 10))
# print(Solution().myPow(2.0, -2))
# print(Solution().myPow(2.0, -3))
# print(Solution().myPow(0.44528, 0))
