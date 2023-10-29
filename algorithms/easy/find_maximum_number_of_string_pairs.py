# 2744. Find Maximum Number of String Pairs

from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pairs = 0
        strings = set()
        for word in words:
            if word in strings:
                pairs += 1
            else:
                strings.add(word[::-1])

        return pairs


sol = Solution().maximumNumberOfStringPairs(
    words=["aa", "ab"])
print(sol)
