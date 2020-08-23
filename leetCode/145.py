# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def recursion(root: TreeNode, res: List[int]):
            if not root:
                return
            if root.left:
                recursion(root.left, res)
            if root.right:
                recursion(root.right, res)

            res.append(root.val)

        recursion(root, res)

        return res