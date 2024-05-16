# 153. Find Minimum in Rotated Sorted Array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_num = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            min_num = min(min_num, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return min(min_num, nums[0])
        
    
sol = Solution().findMin(nums = [3,4,5,1,2])
print(sol)