# 3016. Minimum Number of Pushes to Type Word II

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord("a")] += 1
            
        count.sort(reverse=True)
            
        return sum(count[:8]) + 2 * sum(count[8:16]) + 3 * sum(count[16:24]) + 4 * sum(count[24:])
