# 1038. Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0
        def dfs(n):
            nonlocal s
            if not n:
                return
            
            dfs(n.right)
            s += n.val
            n.val = s
            print(n.val)
            dfs(n.left)
            
        dfs(root)
        return root

root = TreeNode(val=4)
root.left = TreeNode(val=1)
root.right = TreeNode(val=6)
root.left.left = TreeNode(val=0)
root.left.right = TreeNode(val=2)
root.left.right.right = TreeNode(val=3)
root.right.left = TreeNode(val=5)
root.right.right = TreeNode(val=7)
root.right.right.right = TreeNode(val=8)
sol = Solution().bstToGst(root = root)
print(sol)
