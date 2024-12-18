# 496. Next Greater Element I

from typing import List

def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap, stack = {}, []
    for n in nums2:
        while stack and stack[-1] < n:
            hashmap[stack.pop()] = n
        stack.append(n)

    output = [-1] * len(nums1)
    for i, n in enumerate(nums1):
        if n in hashmap:
            output[i] = hashmap[n]
    return output