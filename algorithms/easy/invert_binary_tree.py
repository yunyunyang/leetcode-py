# 226. Invert Binary Tree

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.right, root.left = self.invertTree(
            root.left), self.invertTree(root.right)

        return root


root = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
sol = Solution().invertTree(root)
print(sol)
