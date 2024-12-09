# 3152. Special Array II

from typing import List

def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    prefix = [0] * len(nums)
    for i in range(1, len(nums)):
        if (nums[i - 1] & 1) ^ (nums[i] & 1) == 0:
            prefix[i] = 1
        else:
            prefix[i] = 0

        prefix[i] = prefix[i] + prefix[i - 1]
    
    output = []
    for start, end in queries:
        if prefix[end] - prefix[start] > 0:
            output.append(False)
        else:
            output.append(True)

    return output