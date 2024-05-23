# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for c in t:
            if index == len(s):
                return True
            
            if s[index] == c:
                index += 1
                
        return index == len(s)