# 2278. Percentage of Letter in String

import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return math.floor(s.count(letter)/len(s)*100)
    
sol = Solution().percentageLetter(s = "sgawtb", letter = "s")
print(sol)