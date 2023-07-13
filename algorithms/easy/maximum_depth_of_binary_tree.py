# 104. Maximum Depth of Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

root = TreeNode(val=3, left=TreeNode(val=9, left=TreeNode(val=None), right=TreeNode(val=None)), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
sol = Solution().maxDepth(root)
print(sol)