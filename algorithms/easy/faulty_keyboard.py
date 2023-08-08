# 2810. Faulty Keyboard

class Solution:
    def finalString(self, s: str) -> str:
        if "i" not in s:
            return s
        else:
            while "i" in s:
                i = s.index("i")
                s = s[0:i][::-1] + s[i+1:len(s)]

        return s
    
sol = Solution().finalString(s = "string")
print(sol)