# 3146. Permutation Difference between Two Strings

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        tdict = {}
        for i in range(len(t)):
            tdict[t[i]] = i

        diff = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff += abs(i - tdict[s[i]])
                
        return diff

sol = Solution().findPermutationDifference(s = "abcde", t = "edbac")
print(sol)