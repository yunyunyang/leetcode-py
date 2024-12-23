# 2471. Minimum Number of Operations to Sort a Binary Tree by Level

from typing import Optional
from collections import deque

from algorithms import TreeNode

def minimumOperations(self, root: Optional[TreeNode]) -> int:
    
    def cycleSort(arr):
        sorted_arr = sorted(arr)
        hashmap = {n:i for i, n in enumerate(arr)}
        ops = 0
        for i, n in enumerate(arr):
            if sorted_arr[i] != n:
                j = hashmap[sorted_arr[i]]
                arr[i], arr[j] = arr[j], arr[i]
                hashmap[sorted_arr[i]] = i
                hashmap[n] = j
                ops += 1
                
                # === TLE ===
                # for j in range(i + 1, len(arr)):
                #     if sortedmap[i] == arr[j]:
                #         arr[i], arr[j] = arr[j], arr[i]
                #         ops += 1
        return ops
    
    q, ops = deque([root]), 0
    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ops += cycleSort(level)

    return ops