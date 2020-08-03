"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    first, last = None, None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node: 'Node') -> 'Node':
            if node:
                helper(node.left)
                if self.last:
                    self.last.right = node
                    node.left = self.last
                else:
                    self.first = node
                self.last = node
                helper(node.right)

        if not root:
            return None
        helper(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first
