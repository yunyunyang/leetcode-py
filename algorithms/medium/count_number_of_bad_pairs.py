# 2364. Count Number of Bad Pairs

from typing import List
from collections import defaultdict

def countBadPairs(self, nums: List[int]) -> int:
    count = defaultdict(list)
    for i in range(len(nums)):
        diff = i - nums[i]
        count[diff].append(i)

    total = (len(nums) * (len(nums) - 1)) // 2
    sameVal = 0
    for vals in count.values():
        sameVal += (len(vals) * (len(vals) - 1)) // 2

    return total - sameVal