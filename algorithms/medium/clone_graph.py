# 133. Clone Graph

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map_node = {}

        def dfs(node):
            if node in map_node:
                return map_node[node]

            copy = Node(node.val)
            map_node[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None