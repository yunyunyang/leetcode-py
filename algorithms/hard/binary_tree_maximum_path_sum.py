# 124. Binary Tree Maximum Path Sum

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            nonlocal max_sum
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            max_sum = max(max_sum, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return max_sum