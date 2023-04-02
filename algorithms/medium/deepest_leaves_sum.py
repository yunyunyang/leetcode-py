# 1302. Deepest Leaves Sum

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = deque()
        que.append(root)

        while que:
            output = 0
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

                if not node.left and not node.right and node.val:
                    output += node.val

        return output

root = TreeNode(val=1, 
                left=TreeNode(val=2, 
                              left=TreeNode(val=4, left=TreeNode(val=7), right=TreeNode(val=None)), 
                              right=TreeNode(val=5, left=TreeNode(val=None), right=TreeNode(val=None))), 
                right=TreeNode(val=3, 
                               left=TreeNode(val=None), 
                               right=TreeNode(val=6, left=TreeNode(val=None), right=TreeNode(val=8))))

sol = Solution().deepestLeavesSum(root)
print(sol)