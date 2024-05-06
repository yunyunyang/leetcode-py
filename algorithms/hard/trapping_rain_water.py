# 42. Trapping Rain Water

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right, min_height = [0] * n, [0] * n, [0] * n
        for i in range(1, len(height)):
            if i == 1:
                max_left[i] = height[i - 1]
            else:
                max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            if i == len(height) - 2:
                max_right[i] = height[i + 1]
            else:
                max_right[i] = max(max_right[i + 1], height[i + 1])

        for i in range(len(min_height)):
            n = min(max_left[i], max_right[i]) - height[i]
            min_height[i] = 0 if n < 0 else n

        return sum(min_height)
    
sol = Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])

print(sol)