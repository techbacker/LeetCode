from typing import List
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(idx: int) -> int:
            return nums[idx] - nums[0] - idx

        leftP, rightP = 0, len(nums) - 1

        if k > missing(rightP):
            return nums[rightP] + k - missing(rightP)

        while leftP != rightP:
            pivot = (leftP + (rightP - leftP) // 2)

            # when k > missing(privot)
            if missing(pivot) < k:
                leftP = pivot + 1
            else:
                rightP = pivot

        return nums[leftP - 1] + k - missing(leftP - 1)