# 1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDividable(i):
            if len1 % i == 0 and len2 % i == 0:
                q1 = len1 // i
                q2 = len2 // i
                
                if str2[:i] * q1 == str1 and str2[:i] * q2 == str2:
                    return str2[:i]

        output = None
        for i in range(len2, 0, -1):            
            if isDividable(i) != None:
              output = isDividable(i)
              break

        return output or ""
    
sol = Solution().gcdOfStrings(str1 = "ABABABAB", str2 = "ABAB")
print(sol)