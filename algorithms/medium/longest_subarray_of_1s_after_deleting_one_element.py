# 1493. Longest Subarray of 1's After Deleting One Element

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 and nums[0] != 0:
            return len(nums) - 1
        
        l, r, c, m = 0, 0, 0, 0
        for i in range(len(nums)):
            if i == len(nums) - 1 and nums[i] == 1:
                c += 1
                l = r
                r = c
            if nums[i] == 0:
                l = r
                r = c
                c = 0
            else:
                c += 1

            if l + r > m:
                m = l + r
 
        return m
    
sol = Solution().longestSubarray(nums = [0,0,0])
print(sol)