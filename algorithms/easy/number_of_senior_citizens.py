# 2678. Number of Senior Citizens

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        o = 0
        for i in details:
            o += 1 if int(i[11:13]) > 60 else 0

        return o 
    
sol = Solution().countSeniors(details = ["7868190130M7522","5303914400F9211","9273338290F4010"])
print(sol)