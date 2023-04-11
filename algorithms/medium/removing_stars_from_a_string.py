# 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        o = []
        for i in s:
            if i == '*':
                o.pop()
            else:
                o.append(i)

        return ''.join(o)
    
sol = Solution().removeStars(s = "leet**cod*e")
print(sol)