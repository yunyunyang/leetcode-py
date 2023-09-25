# 11. Container With Most Water

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1

        return area


sol = Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
print(sol)
