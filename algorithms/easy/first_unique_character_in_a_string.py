# 387. First Unique Character in a String

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for k, v in counter.items():
            if v == 1:
                return s.index(k)

        return -1


sol = Solution().firstUniqChar(s = "lleetcode")
print(sol)