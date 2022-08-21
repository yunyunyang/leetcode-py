# 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        output = 0
        cal = 0
        for i in [*s]:
            if i == 'R':
                cal +=1
            if i == 'L':
                cal -=1
            if cal == 0:
                output +=1

        return output

sol = Solution().balancedStringSplit(s = "RLRRLLRLRL")
print(sol)