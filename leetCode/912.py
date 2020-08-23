from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return nums
        res = [[a] for a in nums]
        while len(res) > 1:
            if len(res) % 2 == 0:
                res = [self.merge(res[i], res[i+1]) for i in range(0, len(res) - 1, 2)]
            else:
                # when res is odd number elements, just append the last one and merge all even elements
                last = res[-1]
                res = res[:-1]
                res = [self.merge(res[i], res[i+1]) for i in range(0, len(res) - 1, 2)]
                res.append(last)
        return res[0]

    def merge(self, left_list: List[int], right_list: List[int]) -> List[int]:
        left_i = right_i = 0
        res = []

        while left_i < len(left_list) and right_i < len(right_list):
            if left_list[left_i] < right_list[right_i]:
                res.append(left_list[left_i])
                left_i += 1
            else:
                res.append(right_list[right_i])
                right_i += 1

        if left_i < len(left_list):
            res.extend(left_list[left_i:])
        else:
            res.extend(right_list[right_i:])

        return res

# Solution().sortArray([5,2,3,1])
Solution().sortArray([5,1,1,2,0,0])
