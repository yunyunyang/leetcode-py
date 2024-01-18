# 1207. Unique Number of Occurrences

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence = []
        unique_num = set(arr)
        for n in unique_num:
            occ = arr.count(n)
            if occ not in occurrence:
                occurrence.append(occ)
            else:
                return False
        return True


sol = Solution().uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3])
print(sol)
