# 455. Assign Cookies

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n, i, j = 0, len(g)-1, len(s)-1
        g.sort(reverse=True)
        s.sort(reverse=True)
        print(g)
        print(s)
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                print(s[j], g[j])
                n += 1
                i -= 1
                j -= 1
            else:
                j -= 1

        return n


sol = Solution().findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8])
print(sol)
