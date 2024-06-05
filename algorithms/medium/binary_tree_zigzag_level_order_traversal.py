# 103. Binary Tree Zigzag Level Order Traversal

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        q = deque([root])
        
        index = 0
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                if node and node.right:
                    q.append(node.right)
                if node and node.left:
                    q.append(node.left)
            
            if index % 2 == 0:
                level.reverse()
            
            output.append(level)
            index += 1
            
        return output
    