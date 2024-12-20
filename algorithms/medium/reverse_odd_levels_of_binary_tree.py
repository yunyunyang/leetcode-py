# 2415. Reverse Odd Levels of Binary Tree

from typing import Optional
from collections import deque

from algorithms import TreeNode


# BFS
def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    q, i = deque([root]), 0
    while q:
        if i % 2 == 1:
            l, r = 0, len(q) - 1
            while l < r:
                q[l].val, q[r].val = q[r].val, q[l].val
                l += 1
                r -= 1

        size = len(q)
        for _ in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        i += 1

    return root


# DFS
def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    def dfs(left, right, level):
        if not left or not right:
            return
            
        if level % 2 == 1:
            left.val, right.val = right.val, left.val

        dfs(left.left, right.right, level + 1)
        dfs(left.right, right.left, level + 1)

    dfs(root.left, root.right, 1)
    return root