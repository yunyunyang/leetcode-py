# 1161. Maximum Level Sum of a Binary Tree

from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        
        r = []
        q = collections.deque()
        q.append(root)
        while q:
            le = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    le.append(n.val)
                    q.append(n.left)
                    q.append(n.right)

            if le:
                r.append(sum(le))
        
        return r.index(max(r))+1

root = TreeNode(val=-100, 
                left=TreeNode(val=-200, left=TreeNode(val=-20), right=TreeNode(val=-5)), 
                right=TreeNode(val=-300, left=TreeNode(val=-10)))
sol = Solution().maxLevelSum(root)
print(sol)