# 451. Sort Characters By Frequency

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sort = ""
        for k, v in count.most_common():
            sort += k*v

        return sort


sol = Solution().frequencySort(s="tree")
print(sol)
