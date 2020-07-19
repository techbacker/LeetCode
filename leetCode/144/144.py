# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def recursion(root: TreeNode, result: List[int]) -> List[int]:
            if not root:
                return
            result.append(root.val)
            if root.left:
                recursion(root.left, result)
            if root.right:
                recursion(root.right, result)
        recursion(root, result)
        return result