# 111. Minimum Depth of Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
# root = [3,9,20,null,null,15,7]
root = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
sol = Solution().minDepth(root = root)
print(sol)