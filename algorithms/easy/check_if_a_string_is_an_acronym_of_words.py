# 2828. Check if a String Is an Acronym of Words

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        acronym = ""
        for w in words:
            acronym += w[0]

        return acronym == s


sol = Solution().isAcronym(words=["alice", "bob", "charlie"], s="abc")
print(sol)
