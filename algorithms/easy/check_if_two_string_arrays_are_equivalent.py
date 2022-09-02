# 1662. Check If Two String Arrays are Equivalent

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

sol = Solution().arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"])
print(sol)