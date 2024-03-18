# 66. Plus One

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break

        if digits.count(0) == len(digits):
            digits.insert(0, 1)

        return digits


sol = Solution().plusOne(digits=[9,8,9])
print(sol)
