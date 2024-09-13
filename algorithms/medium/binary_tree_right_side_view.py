# 199. Binary Tree Right Side View

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        q = deque([root])

        while q:
            right_node = None
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node:
                    right_node = node
                    q.append(node.left)
                    q.append(node.right)

            if right_node:
                output.append(right_node.val)

        return output