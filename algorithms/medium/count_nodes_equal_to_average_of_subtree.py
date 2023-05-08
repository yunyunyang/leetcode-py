# 2265. Count Nodes Equal to Average of Subtree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        o, s, c = 0, 0, 0
        def dfs(n):
            nonlocal o, s, c
            if not n:
                return 0, 0

            lc, ls = dfs(n.left)
            rc, rs = dfs(n.right)
            
            c = lc + rc + 1
            s = ls + rs + n.val

            if s // c == n.val:
                o += 1

            return c, s

        dfs(root)
        return o
    
 
root = TreeNode(val=4)
root.left = TreeNode(val=8)
root.right = TreeNode(val=5)
root.left.left = TreeNode(val=0)
root.left.right = TreeNode(val=1)
root.right.right = TreeNode(val=6)
sol = Solution().averageOfSubtree(root)
print(f'sol = {sol}')