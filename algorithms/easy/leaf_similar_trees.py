# 872. Leaf-Similar Trees

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1, leaf2 = [], []

        def dfs(node, flag):
            if not node:
                return

            nonlocal leaf1, leaf2
            if flag == True and node.left is None and node.right is None:
                leaf1.append(node.val)

            if flag == False and node.left is None and node.right is None:
                leaf2.append(node.val)

            dfs(node.left, flag)
            dfs(node.right, flag)

        dfs(root1, True)
        dfs(root2, False)

        return leaf1 == leaf2
