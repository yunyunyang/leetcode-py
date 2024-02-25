# 1305. All Elements in Two Binary Search Trees

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        elt = []
        
        def traverse(node):
            if not node:
                return 
            elt.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root1)
        traverse(root2)
        elt.sort()
            
        return elt

r1 = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=4))
r2 = TreeNode(val=2, left=TreeNode(val=0), right=TreeNode(val=3))
sol = Solution().getAllElements(r1, r2)
print(sol)