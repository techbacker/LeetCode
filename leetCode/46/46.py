class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n:
                result.append(nums[:])

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                print(nums, first, i)
                backtrack(first + 1)
                # restore parent node state
                nums[first], nums[i] = nums[i], nums[first]

        result = []
        n = len(nums)
        backtrack()
        return result