# 2942. Find Words Containing Character

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for i, w in enumerate(words):
            if w.count(x) > 0:
                output.append(i)

        return output


sol = Solution().findWordsContaining(words=["leet", "code"], x="e")
print(sol)
