# 2090. K Radius Subarray Averages

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        if len(nums) < k * 2 + 1:
            return [-1] * len(nums)
            
        o, n = [], k*2+1
        s = sum(nums[:k*2+1])
        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                o.append(-1)
            else:
                if i > k:
                    s = s - nums[i-k-1] + nums[i+k]
                o.append(s//n)

        return o
    
sol = Solution().getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3)
print(sol)