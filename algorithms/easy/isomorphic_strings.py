# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return

        smap, tmap = [-1] * 256, [-1] * 256
        for i in range(len(s)):
            if smap[ord(s[i])] != tmap[ord(t[i])]:
                return False

            smap[ord(s[i])] = i
            tmap[ord(t[i])] = i

        return True


sol = Solution().isIsomorphic(s="paper", t="title")
print(sol)
