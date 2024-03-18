# 2864. Maximum Odd Binary Number

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1') - 1
        max_number = ''
        for i in range(len(s) - 1):
            if ones > 0:
                max_number += '1'
                ones -= 1
            else:
                max_number += '0'

        return max_number + '1'


sol = Solution().maximumOddBinaryNumber(s="0101")
print(sol)
