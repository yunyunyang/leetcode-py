# 242. Valid Anagram

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)


sol = Solution().isAnagram(s = "anagram", t = "nagaram")
print(sol)