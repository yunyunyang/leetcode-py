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

        q = deque()
        if root:
            q.append(root)
            
        while q:
            right_node = None
            for _ in range(len(q)):
                node = q.popleft()
                right_node = node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            output.append(right_node)
            
        return output