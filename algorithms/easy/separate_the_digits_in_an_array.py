# 2553. Separate the Digits in an Array

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for n in nums:
            tmp = []
            while n > 0:
                tmp.append(n%10)
                n //= 10
               
            output += reversed(tmp)
                
        return output
    

sol = Solution().separateDigits(nums = [13,25,83,77])
print(sol)