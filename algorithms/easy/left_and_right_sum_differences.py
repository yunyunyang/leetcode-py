# 2574. Left and Right Sum Differences

from typing import List

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        s = len(nums)
        ls, rs = [0], [0]
        for i in range(0, s-1):
            ls.append(ls[i] + nums[i])

        nums.reverse()
        for i in range(0, s-1):
            rs.append(rs[i] + nums[i])
        rs.reverse()
            
        return [abs(l-r) for l, r in zip(ls, rs)]
    
sol = Solution().leftRigthDifference(nums = [10,4,8,3])
print(sol)