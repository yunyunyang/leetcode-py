# 1481. Least Number of Unique Integers after K Removals

from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        imap = {}
        for i in arr:
            imap[i] = imap.get(i, 0) + 1

        smap = sorted(imap.items(), key=lambda x: x[1])
        for key, value in smap:
            if value <= k:
                k -= value
                del imap[key]
            else:
                break

        return len(imap)


sol = Solution().findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3)
print(sol)
