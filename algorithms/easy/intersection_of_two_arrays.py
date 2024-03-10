# 349. Intersection of Two Arrays

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = list(set(nums1)), list(set(nums2))

        common = []
        if len(nums1) <= len(nums2):
            for n in nums1:
                if n in nums2:
                    common.append(n)
        else:
            for n in nums2:
                if n in nums1:
                    common.append(n)

        return common


sol = Solution().intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])
print(sol)
