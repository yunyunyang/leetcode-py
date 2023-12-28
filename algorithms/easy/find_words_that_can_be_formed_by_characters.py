# 1160. Find Words That Can Be Formed by Characters

from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charnum = {}
        for c in chars:
            if c not in charnum:
                charnum[c] = 1
            else:
                charnum[c] += 1

        count = 0
        for w in words:
            dummy = charnum.copy()
            for c in w:
                if c in dummy and dummy[c] > 0:
                    dummy[c] -= 1
                else:
                    count -= len(w)
                    break

            count += len(w)

        return count


sol = Solution().countCharacters(
    words=["cat", "bt", "hat", "tree"], chars="atach")

print(sol)
