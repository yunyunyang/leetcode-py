# 2396. Strictly Palindromic Number

import numpy as np

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        output = True
        for i in range(2, n-1):
            num = np.base_repr(n, base=i)
            rev = num[::-1]

            if int(num) ^ int(rev) != 0:
                return False
                
        return output


sol = Solution().isStrictlyPalindromic(n = 4)
print(sol)