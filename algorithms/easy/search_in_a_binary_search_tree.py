# 700. Search in a Binary Search Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while(node):

            if node.val == val:
                return node
            if node.val < val:
                node = node.right
            else:
                node = node.left

        return None
     

root = TreeNode(val=4)
root.left = TreeNode(val=2)
root.right = TreeNode(val=7)
root.left.left = TreeNode(val=1)
root.left.right = TreeNode(val=3)
sol = Solution().searchBST(root = root, val = 2)
print(type(sol))