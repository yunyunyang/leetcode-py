# 2744. Find Maximum Number of String Pairs

from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        o = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] == words[j][::-1]:
                    o += 1
                    
        return o
    
sol = Solution().maximumNumberOfStringPairs(words = ["aa","ab"])
print(sol)