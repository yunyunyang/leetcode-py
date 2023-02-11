# 2351. First Letter to Appear Twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict_letter = {}
        for i in range(len(s)):
            char = s[i]
            if char not in dict_letter.keys():
                dict_letter[char] = 1
            else:
                return char

sol = Solution().repeatedCharacter(s = "abccbaacz")
print(sol)