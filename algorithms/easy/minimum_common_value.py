# 2540. Minimum Common Value

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = float('inf')
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common = nums1[i]
                break
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return common if common != float('inf') else -1


sol = Solution().getCommon(nums1=[1, 2], nums2=[2, 4])
print(sol)
