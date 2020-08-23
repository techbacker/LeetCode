from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
             return []
        return self.dfs(1,n)

    def dfs(self,start,end):
        res = []
        if start > end:
            res.append(None)
            return res

        for i in range(start, end+1):
            left_list = self.dfs(start, i-1)
            right_list = self.dfs(i+1, end)
            for l in left_list:
                for r in right_list:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res

Solution().generateTrees(3)
