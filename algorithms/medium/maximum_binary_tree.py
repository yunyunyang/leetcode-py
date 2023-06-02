# 654. Maximum Binary Tree

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        stack = []
        for n in nums:
            node = TreeNode(n)
            while stack and n > stack[-1].val:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]

sol = Solution().constructMaximumBinaryTree(nums = [3,2,1,6,0,5])
