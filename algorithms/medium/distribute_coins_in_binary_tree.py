# 979. Distribute Coins in Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            
            # Calculate the coins each subtree has available to exchange
            left_coins = dfs(node.left)
            right_conis = dfs(node.right)

            # Add the total number of exchanges to moves
            self.moves += abs(left_coins) + abs(right_conis)

            # The number of coins current has available to exchange
            return (node.val - 1) + left_coins + right_conis
            
        dfs(root)
        
        return self.moves

root = TreeNode(val=3, left=TreeNode(val=0), right=TreeNode(val=0))
sol = Solution().distributeCoins(root)
print(sol)