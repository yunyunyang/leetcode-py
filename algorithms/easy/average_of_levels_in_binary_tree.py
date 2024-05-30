# 637. Average of Levels in Binary Tree

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        average = []
        q = deque([root])
        
        while q:
            s, c = 0, 0
            for i in range(len(q)):
                node = q.popleft()
                s += node.val
                c += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            average.append(s / c)
        
        return average
            