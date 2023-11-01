# 501. Find Mode in Binary Search Tree

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes, output = {}, []

        def dfs(node):
            if not node:
                return 0

            if node.val not in modes:
                modes[node.val] = 1
            else:
                modes[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_mode = max(modes.values())
        for k, v in modes.items():
            if v == max_mode:
                output.append(k)

        return output


root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=2)))
sol = Solution().findMode(root)
print(sol)
