#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# @lc code=start

# time complexity: O(m+n) constant, space complexity: O(min(m, n))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        dictionary = {}
        result = []

        for x in nums1:
            if dictionary.get(str(x)) == None:
                dictionary[str(x)] = 1
            else:
                dictionary[str(x)] = dictionary.get(str(x)) + 1

        for y in range(0, len(nums2)):
            index = str(nums2[y])
            if dictionary.get(index) is not None and dictionary.get(index) > 0:
                result.append(nums2[y])
                dictionary[index] = dictionary.get(index) - 1

        return result

# @lc code=end

