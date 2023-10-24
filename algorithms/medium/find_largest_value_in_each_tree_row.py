# 515. Find Largest Value in Each Tree Row

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = deque()
        que.append(root)

        output = []

        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

                level.append(node.val)
            output.append(max(level))

        return output


root = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5), right=TreeNode(val=3)),
                right=TreeNode(val=2, right=TreeNode(val=9)))
sol = Solution().largestValues(root)
print(sol)
