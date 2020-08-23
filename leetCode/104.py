# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.count = 0
        def rec(root: TreeNode, depth: int):
            if not root:
                return
            if not root.right and not root.left:
                self.count = max(self.count, depth)
            if root.left:
                rec(root.left, depth + 1)
            if root.right:
                rec(root.right, depth + 1)
        rec(root, 1)
        return self.count