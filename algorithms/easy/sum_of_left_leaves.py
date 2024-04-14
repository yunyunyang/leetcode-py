# 404. Sum of Left Leaves

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leaves = 0

        def dfs(node, which):
            if not node:
                return

            nonlocal leaves
            if which and not node.left and not node.right:
                leaves += node.val

            dfs(node.left, 1)
            dfs(node.right, 0)

        dfs(root, 0)
        return leaves


root = TreeNode(val=3,
                left=TreeNode(val=9),
                right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
sol = Solution().sumOfLeftLeaves(root)
print(sol)
