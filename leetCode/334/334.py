from typing import List


class Solution:
    def recursion(self, s: List[str], index: int) -> None:
        if index > len(s) / 2 - 1:
            return
        tmp = s[index]
        s[index] = s[len(s) - 1 - index]
        s[len(s) - 1 - index] = tmp
        self.recursion(s, index + 1)

    def reverseString(self, s: List[str]) -> None:
        """
      Do not return anything, modify s in-place instead.
      """
        self.recursion(s, 0)
        print(s)
        return None


Solution().reverseString(['h', 'e', 'l', 'l', 'o'])
Solution().reverseString(['H', 'a', 'n', 'n', 'a', 'h'])
