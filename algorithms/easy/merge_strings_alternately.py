# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        s = min(len(word1), len(word2))
        for i in range(s):
            output += word1[i] + word2[i]
            
        output += word1[s:] + word2[s:]
        return output


sol = Solution().mergeAlternately(word1 = "abc", word2 = "pqr")
print(sol)