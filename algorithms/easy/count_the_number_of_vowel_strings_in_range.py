# 2586. Count the Number of Vowel Strings in Range

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        o = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        for i in range(left, right + 1):
            if (words[i][0] in vowel) and (words[i][-1] in vowel):
                o += 1

        return o
    
sol = Solution().vowelStrings(words = ["are","amy","u"], left = 0, right = 2)
print(sol)