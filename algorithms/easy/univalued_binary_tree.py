# 965. Univalued Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        v = root.val
        f = True

        def dfs(node):
            if not node:
                return
            
            nonlocal f
            if node.val is not None and node.val != v:
                f = False
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return f
    
root = TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=1), right=TreeNode(val=1)), right=TreeNode(val=1, left=TreeNode(val=None), right=TreeNode(val=1)))
sol = Solution().isUnivalTree(root)
print(sol)