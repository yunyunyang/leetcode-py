# 144. Binary Tree Preorder Traversal

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def dfs(node):
            nonlocal l
            if not node:
                return l
            
            if node.val != None:
                print(node.val)
                l.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return l

root = TreeNode(val=0, left=TreeNode(val=None), right=TreeNode(val=2, left=TreeNode(val=3)))
sol = Solution().preorderTraversal(root)
print(sol)