class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(first: int = 1, curr: List[int] = []):
            # if combination is done
            if len(curr) == k:
                output.append(curr[:])

            # iterate over the integers form first to n
            for i in range(first, n + 1):
                # add integer i into the current combination curr
                curr.append(i)
                # proceed to add more integers into the combination
                backtracking(i+1, curr)
                # backtrack by removing i from curr
                curr.pop()

        output = []
        backtracking()
        return output
