# 429. N-ary Tree Level Order Traversal

from typing import List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []
        
        q = deque()
        if root:
            q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                children = node.children
                for child in children:
                    q.append(child)

            output.append(level)

        return output