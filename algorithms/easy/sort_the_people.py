# 2418. Sort the People

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = dict(zip(heights, names))
        sorted_pairs = dict(sorted(pairs.items(), reverse=True))
        return sorted_pairs.values()


sol = Solution().sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150])
print(sol)