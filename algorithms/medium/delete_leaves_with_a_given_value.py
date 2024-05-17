# 1325. Delete Leaves With a Given Value

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        if not root.left and not root.right and root.val == target:
            return None
            
        return root
    

root = TreeNode(val=1, 
                left=TreeNode(val=2, left=TreeNode(val=2)), 
                right=TreeNode(val=3, left=TreeNode(val=2), right=TreeNode(val=4)))    
sol = Solution().removeLeafNodes(root, 2)
print(sol)