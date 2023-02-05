# 2331. Evaluate Boolean Binary Tree
# Postorder Traversal

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            return True if root.val else False
    

sol = Solution().evaluateTree(TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3, left=TreeNode(val=0), right=TreeNode(val=1))))
print(sol)