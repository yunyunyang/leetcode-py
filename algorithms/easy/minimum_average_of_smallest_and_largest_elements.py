# 3194. Minimum Average of Smallest and Largest Elements

from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left, right = 0, len(nums) - 1
        min_avg = float('inf')
        while left <= right:
            min_avg = min(min_avg, (nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
            
        return min_avg
    
sol = Solution().minimumAverage(nums = [7,8,3,4,15,13,4,1])
print(sol)