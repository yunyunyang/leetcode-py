# 1684. Count the Number of Consistent Strings

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        not_allowed = 0
        for i in words:
            for j in [*allowed]:
                i = i.replace(j, "")
            if len(i) > 0:
                not_allowed += 1
        return len(words) - not_allowed

sol = Solution().countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])
print(sol)