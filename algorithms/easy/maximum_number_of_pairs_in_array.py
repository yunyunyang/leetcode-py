# 2341. Maximum Number of Pairs in Array

from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        map = {}
        output = [0, 0]
        for i in nums:
            if i in map.keys():
                map[i] += 1
            else:
                map[i] = 1

        for i in map.values():
            output[0] = output[0] + i//2
            if i%2 == 1:
                output[1] += 1
        
        return output
    

sol = Solution().numberOfPairs(nums = [1,3,2,1,3,2,2])
print(sol)