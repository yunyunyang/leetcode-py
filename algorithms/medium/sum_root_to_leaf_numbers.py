# 129. Sum Root to Leaf Numbers

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, s):
            if not node:
                return 0

            s = s * 10 + node.val
            if not node.left and not node.right:
                return s

            return dfs(node.left, s) + dfs(node.right, s)

        return dfs(root, 0)
  
root = TreeNode(val=4, 
                left=TreeNode(val=9, left=TreeNode(val=5), right=TreeNode(val=1)),
                right=TreeNode(val=0))
root = TreeNode(val=9)
sol = Solution().sumNumbers(root)
print(sol)