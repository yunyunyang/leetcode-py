# 88. Merge Sorted Array

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]

        nums1.sort()
    
sol = Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1)