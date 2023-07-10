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
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if l > 0 and r > 0:
            return 1 + min(l, r)
        if l == 0:
            return 1 + r
        if r == 0:
            return 1 + l
    
# root = [3,9,20,null,null,15,7]
# root = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
root = TreeNode(val=2, left=None, right=TreeNode(val=3, left=None, right=TreeNode(val=4, left=None, right=TreeNode(val=5, left=None, right=TreeNode(val=6)))))
sol = Solution().minDepth(root = root)
print(sol)