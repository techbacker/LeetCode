class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = []
        i, j= 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_arr.append(nums1[i])
                i += 1
            else:
                sorted_arr.append(nums2[j])
                j += 1

        sorted_arr.extend(nums1[i:]) if i < len(nums1) else sorted_arr.extend(nums2[j:])

        print(sorted_arr)
        if len(sorted_arr) % 2 == 1:
            return sorted_arr[len(sorted_arr) // 2]
        else:
            return (sorted_arr[len(sorted_arr) // 2] + sorted_arr[len(sorted_arr) // 2 - 1]) / 2

