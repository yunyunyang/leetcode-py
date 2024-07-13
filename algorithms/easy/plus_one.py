# 66. Plus One

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        i, one = 0, 1

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1

        return digits[::-1]


sol = Solution().plusOne(digits=[9,8,9])
print(sol)
