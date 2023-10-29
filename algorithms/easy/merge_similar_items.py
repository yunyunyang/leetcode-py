# 2363. Merge Similar Items

from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        merge_items = {}
        items = items1 + items2
        for k, v in items:
            if k not in merge_items:
                merge_items[k] = v
            else:
                merge_items[k] += v

        output = []
        for k, v in merge_items.items():
            output.append([k, v])

        output = sorted(output)
        return output


sol = Solution().mergeSimilarItems(
    items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]])
print(sol)
