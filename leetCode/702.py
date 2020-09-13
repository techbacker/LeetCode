# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 10000
        while left <= right:
            mid = left + (right - left) // 2
            value = reader.get(mid)
            if value == 2147483647:
                right = mid - 1
            else:
                if value == target:
                    return mid
                elif value < target:
                    left = mid + 1
                elif value >= target:
                    right = mid - 1
        return -1
