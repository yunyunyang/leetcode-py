# 2215. Find the Difference of Two Arrays

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1, n2 = set(nums1), set(nums2)
        return [list(n1-n2), list(n2-n1)]
    
sol = Solution().findDifference(nums1 = [1,2,3], nums2 = [2,4,6])
print(sol)