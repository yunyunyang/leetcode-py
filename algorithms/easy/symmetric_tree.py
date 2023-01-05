# 101. Symmetric Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.mirror(root.left, root.right)

    def mirror(self, left: TreeNode, right: TreeNode):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left and right and left.val != right.val:
            return False
        else:
            return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)

sol = Solution().isSymmetric(root=TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=2)))
print(sol)