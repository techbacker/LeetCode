class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def mapping(digit):
            phone = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}
            return phone[digit]

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            else:
                for letter in mapping(next_digits[0]):
                    solution = combination + letter
                    backtrack(solution, next_digits[1:])

        result = []
        if digits:
            backtrack('', digits)
        return result