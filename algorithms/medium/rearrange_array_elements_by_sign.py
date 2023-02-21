# 2149. Rearrange Array Elements by Sign

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        output = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)

        for i in range(len(nums)//2):
            output.append(pos[i])
            output.append(neg[i])

        return output
    

sol = Solution().rearrangeArray(nums = [3,1,-2,-5,2,-4])
print(sol)
        