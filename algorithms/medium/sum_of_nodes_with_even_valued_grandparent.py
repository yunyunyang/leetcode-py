# 1315. Sum of Nodes with Even-Valued Grandparent

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        o = 0
        def dfs(n, p, gp):
            nonlocal o
            if not n:
                return
            
            if gp and gp.val % 2 == 0:
                o += n.val

            dfs(n.left, n, p)
            dfs(n.right, n, p)
            
        dfs(root, None, None)
        return o

root = TreeNode(val=6)
root.left = TreeNode(val=7)
root.right = TreeNode(val=8)
root.left.left = TreeNode(val=2)
root.left.right = TreeNode(val=7)
root.left.left.left = TreeNode(val=9)
root.left.right.left = TreeNode(val=1)
root.left.right.right = TreeNode(val=4)
root.right.left = TreeNode(val=1)
root.right.right = TreeNode(val=3)
root.right.right.right = TreeNode(val=5)
sol = Solution().sumEvenGrandparent(root)
print(sol)