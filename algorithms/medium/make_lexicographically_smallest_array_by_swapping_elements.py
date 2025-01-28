# 2948. Make Lexicographically Smallest Array by Swapping Elements

from typing import List
from collections import deque

def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
    groups = []
    num_of_group = {}
    for n in sorted(nums):
        if not groups or abs(n - groups[-1][-1]) > limit:
            groups.append(deque())
        groups[-1].append(n)
        num_of_group[n] = len(groups) - 1
    
    res = []
    for n in nums:
        i = num_of_group[n]
        res.append(groups[i].popleft())
    
    return res