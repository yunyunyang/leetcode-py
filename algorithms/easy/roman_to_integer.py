# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        roman = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)-1):
            if roman[s[i]] >= roman[s[i+1]]:
                output += roman[s[i]]
            else:
                output -= roman[s[i]]
            
        return output + roman[s[-1]]


sol = Solution().romanToInt(s = "MCMXCIV")
print(sol)