# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        o = ""
        s = min(len(word1), len(word2))
        for i in range(s):
            o += word1[i] + word2[i]
        o += word1[s:] + word2[s:]

        return o

sol = Solution().mergeAlternately(word1 = "abc", word2 = "pqr")
print(sol)