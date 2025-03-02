# 2570. Merge Two 2D Arrays by Summing Values

from typing import List

def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    counter = {}
    for num in nums1:
        counter[num[0]] = num[1]
    for num in nums2:
        counter[num[0]] = counter.get(num[0], 0) + num[1]

    res = []
    for k, v in sorted(counter.items()):
        res.append([k, v])

    return res