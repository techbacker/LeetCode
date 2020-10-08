#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
# #
# from typing import List
# # @lc code=start
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root is None or val == root.val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        if val > root.val:
            return self.searchBST(root.right, val)

    def iterationBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right

        return root

# s = Solution()
# result = s.searchBST([4,2,7,1,3], 2)
# print(result)
# @lc code=end

