# 590. N-ary Tree Postorder Traversal

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []

        def dfs(node):
            if not node:
                return None

            for n in node.children:
                dfs(n)
            output.append(node.val)

        dfs(root)
        return output


root = Node(val=1, children=[Node(val=3, children=[
            Node(val=5), Node(val=6)]), Node(val=2), Node(val=4)])
sol = Solution().postorder(root)
print(sol)
