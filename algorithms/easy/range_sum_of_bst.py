# 938. Range Sum of BST

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        def dfs(node):
            if not node:
                return 0
            
            nonlocal sum
            if node.val and node.val >= low and node.val <= high:
                print(node.val)
                sum += node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return sum

root = TreeNode(val=10, left=TreeNode(val=5, left=TreeNode(val=3), right=TreeNode(val=7)), right=TreeNode(val=15, left=TreeNode(val=None), right=TreeNode(val=18)))
sol = Solution().rangeSumBST(root = root, low = 7, high = 15)
print(sol)