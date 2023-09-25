# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = s+t
        m = {}
        for i in n:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        for k in m.keys():
            if m[k] % 2 != 0:
                return k


sol = Solution().findTheDifference(s="abcd", t="abcde")
print(sol)
