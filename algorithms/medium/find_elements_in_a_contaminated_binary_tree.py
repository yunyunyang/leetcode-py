# 1261. Find Elements in a Contaminated Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

def __init__(self, root: Optional[TreeNode]):
    self.seen = set()
    self.dfs(root, 0)

def find(self, target: int) -> bool:
    return target in self.seen

def dfs(self, node, count):
    if node is None:
        return

    self.seen.add(count)
    self.dfs(node.left, count * 2 + 1)
    self.dfs(node.right, count * 2 + 2)