# 94. Binary Tree Inorder Traversal

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def dfs(node):
            nonlocal l
            if not node:
                return l
            
            dfs(node.left)
            if node.val is not None:
                l.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return l
    
root = TreeNode(val=0, left=TreeNode(val=None), right=TreeNode(val=2, left=TreeNode(val=3)))
sol = Solution().inorderTraversal(root)
print(sol)