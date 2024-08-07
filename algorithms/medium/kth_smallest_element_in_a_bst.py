# 230. Kth Smallest Element in a BST

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = -1
        
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            nonlocal k, output
            k = k - 1
            if k == 0:
                output = node.val
            dfs(node.right)
        
        dfs(root)
        return output