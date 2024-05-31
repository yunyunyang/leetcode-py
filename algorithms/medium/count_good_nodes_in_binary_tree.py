# 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        
        def dfs(node, x):
            if not node:
                return 0
            
            nonlocal good
            if node.val >= x:
                x = max(x, node.val)
                good += 1
            
            dfs(node.left, x)
            dfs(node.right, x)
            
        dfs(root, root.val)
        return good