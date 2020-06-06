class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return self.rec(N, K, 1, [0])

    def rec(self, N: int, K: int, row: int, symbol) -> int:
        # base case
        if N == row:
            return symbol[K-1]

        for i in range(len(symbol)):
            symbol.append(1 if symbol[i] is 0 else 0)
            print(symbol, f'k {K}, len {len(symbol)}, i {i}')
            if len(symbol) == K:
                return symbol[K-1]
        return self.rec(N, K, row+1, symbol)


# print(Solution().kthGrammar(1,1))
# print(Solution().kthGrammar(2,1))
# print(Solution().kthGrammar(2,2))
# print(Solution().kthGrammar(3,3))
# print(Solution().kthGrammar(4,5))
print(5&1)
print(4&1)
print(3&1)
print(2&1)
print(100&1)