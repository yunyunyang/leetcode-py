# 513. Find Bottom Left Tree Value

from typing import Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        queue = deque([root])
        bottom_node = None

        while queue:
            bottom_node = queue.popleft()

            if bottom_node.right:
                queue.append(bottom_node.right)

            if bottom_node.left:
                queue.append(bottom_node.left)

        return bottom_node.val


# root = TreeNode(val=1,
#                 left=TreeNode(val=2, left=TreeNode(val=4)),
#                 right=TreeNode(val=3, left=TreeNode(val=5, left=TreeNode(val=7)), right=TreeNode(val=6)))
root = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
sol = Solution().findBottomLeftValue(root)
print(sol)
