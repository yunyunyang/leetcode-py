# 1897. Redistribute Characters to Make All Strings Equal

from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True

        char_count = sum(len(w) for w in words)
        if char_count % len(words) != 0:
            return False

        char_map = [0] * 26
        for w in words:
            for c in w:
                char_map[ord(c) - ord('a')] += 1

        for i in char_map:
            if i % len(words) != 0:
                return False

        return True


sol = Solution().makeEqual(words=["abc", "aabc", "bc"])
print(sol)
