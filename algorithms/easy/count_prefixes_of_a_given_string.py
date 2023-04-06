# 2255. Count Prefixes of a Given String

from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:    
        o = 0
        for i in range(len(words)):
            if len(s) >= len(words[i]) and words[i] in s and s.index(words[i]) == 0:
                    o += 1

        return o
    
sol = Solution().countPrefixes(words = ["e","s","mi","e","ia","ibwu","e","e","k","ci","rip","suw","a","l"], s = "e")

print(sol)