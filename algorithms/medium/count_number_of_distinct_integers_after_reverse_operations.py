# 2442. Count Number of Distinct Integers After Reverse Operations

from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            if n < 10:
                nums.append(n)
            else:
                rn = 0
                while n > 0:
                    r = n % 10
                    rn = (rn * 10) + r
                    n //= 10

                nums.append(rn)

        return len(set(nums))

sol = Solution().countDistinctIntegers(nums = [1,13,10,12,31])
print(sol)