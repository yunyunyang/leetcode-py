# 1941. Check if All Characters Have Equal Number of Occurrences

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for i in range(len(s)):
            letter = s[i]
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
        
        base = next(iter(dic.values()))
        for i in dic.values():
            if i != base:
                return False
            
        return True


sol = Solution().areOccurrencesEqual(s = "abacbc")
print(sol)