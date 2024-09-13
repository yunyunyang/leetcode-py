# 543. Diameter of Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.output = 0

        # Returns the depth of the current node
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.output = max(self.output, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.output
    
sol = Solution().diameterOfBinaryTree()
print(sol)