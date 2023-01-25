# 2535. Difference Between Element Sum and Digit Sum of an Array

from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = digit_sum = 0
        for i in nums:
            element_sum += i
            while i > 0:
                digit_sum += i % 10
                i //= 10

        return element_sum - digit_sum


sol = Solution().differenceOfSum(nums = [1,15,6,3])
print(sol)